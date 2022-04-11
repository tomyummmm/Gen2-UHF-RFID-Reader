#Developed by: Nikos Kargas

from gnuradio import gr
from gnuradio import uhd
from gnuradio import blocks
from gnuradio import filter
from gnuradio import analog
from gnuradio import digital
from gnuradio import qtgui
import rfid
import os

import limesdr

# debug
import numpy as np
import matplotlib.pyplot as plt

# DEBUG = False
DEBUG = True

# data transfer lib
from gnuradio import blocks
from gnuradio import zeromq
import array
import zmq
socket_str = "tcp://127.0.0.1:5557"

from ZMQ_pub_api import Publisher
import random

# data plot lib
# import cv2
import numpy as np
import time


# data transfer code
def zmq_consumer(pub):
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.connect(socket_str)
    # Sleep for 0.5 seconds to ensure connection is finished, 
    # .connect function returns before connection is fully made, causing first set of data to miss.
    time.sleep(0.5)
    while True:
        raw_data = results_receiver.recv()
        # char_bits
        chars = array.array('b', raw_data)
        epc = ""
        for char in chars:
            epc += chr(char)
        if len(epc) == 128:
            # convert bit string to hex starting
            epc_hex = hex(int(epc, 2))[2:]
            print("32 digit raw data: ", epc_hex)
            # Remove PC (starting 4 hex digits) and CRC16 (last 4 hex digits)
            epc_hex = epc_hex[4:-4]
            # Simulate RSSI data with random values
            RSSI = str(round(random.uniform(-35,-50), 3))
            print("24 digit EPC: ", epc_hex)
            pub.publish(epc_0x_str=epc_hex, rssi_str=RSSI, time_delay_s=2)



class reader_top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        #rt = gr.enable_realtime_scheduling()

        ######## Variables #########
        self.dac_rate = 1e6  # DAC rate
        self.adc_rate = 2e6  # ADC rate (2MS/s complex samples)
        self.decim = 5  # Decimation (downsampling factor)
        self.ampl = 0.1  # original: 0.1, Output signal amplitude (signal power vary for different RFX900 cards)
        self.freq = 910e6  # Modulation frequency (can be set between 902-920)
        self.rx_gain = 50  # RX Gain (gain at receiver)  TXY: dB
        self.tx_gain = 30  # RFX900 no Tx gain option  TXY: dB
        self.rx_bw = 1e6
        self.tx_bw = 1e6
        self.cal_bw = 2.5e6
        self.freq_off = 0 # 0.2e6

        # Each FM0 symbol consists of ADC_RATE/BLF samples (2e6/40e3 = 50 samples)
        # TXY: BLF 40 kHz
        # 10 samples per symbol after matched filtering and decimation
        self.num_taps = [1] * 25 # matched to half symbol period

        ######## File sinks for debugging (1 for each block) #########
        # self.file_sink_source         = blocks.file_sink(gr.sizeof_gr_complex*1, "../misc/data/source", False)
        cwd = os.getcwd()
        # print(cwd)
        self.file_sink_source = blocks.file_sink(gr.sizeof_gr_complex*1, cwd + os.sep + "../misc/data/source_i2r", False)
        # self.file_sink_matched_filter = blocks.file_sink(gr.sizeof_gr_complex*1, cwd + os.sep + "misc/data/matched_filter", False)
        # self.file_sink_gate = blocks.file_sink(gr.sizeof_gr_complex*1, cwd + os.sep + "misc/data/gate", False)
        # self.file_sink_decoder = blocks.file_sink(gr.sizeof_gr_complex*1, cwd + os.sep + "misc/data/decoder", False)
        # self.file_sink_reader = blocks.file_sink(gr.sizeof_float*1, cwd + os.sep + "misc/data/reader", False)

        ######## Blocks #########

        # self.limesdr_source_0 = limesdr.source('', 0, '', False)
        # self.limesdr_source_0.set_sample_rate(self.adc_rate)
        # self.limesdr_source_0.set_center_freq(self.freq, 0)
        # self.limesdr_source_0.set_bandwidth(self.rx_bw, 0)
        # self.limesdr_source_0.set_digital_filter(self.adc_rate 0)
        # self.limesdr_source_0.set_gain(self.rx_gain, 0)
        # self.limesdr_source_0.set_antenna(255, 0)
        # self.limesdr_source_0.calibrate(self.cal_bw , 0)

        # self.limesdr_sink_1 = limesdr.sink('', 0, '', '')
        # self.limesdr_sink_1.set_sample_rate(self.dac_rate)
        # self.limesdr_sink_1.set_center_freq(self.freq + self.freq_off, 0)
        # self.limesdr_sink_1.set_bandwidth(self.tx_bw, 0)
        # self.limesdr_sink_1.set_digital_filter(self.adc_rate, 0)
        # self.limesdr_sink_1.set_gain(self.tx_gain, 0)
        # self.limesdr_sink_1.set_antenna(255, 0)
        # self.limesdr_sink_1.calibrate(self.cal_bw, 0)

        self.matched_filter = filter.fir_filter_ccc(self.decim, self.num_taps);
        self.gate = rfid.gate(int(self.adc_rate/self.decim))
        #self.gate = rfid.gate(int(self.adc_rate))
        self.tag_decoder = rfid.tag_decoder(int(self.adc_rate/self.decim))
        self.reader = rfid.reader(int(self.adc_rate/self.decim),int(self.dac_rate))
        self.amp = blocks.multiply_const_ff(self.ampl)
        self.to_complex = blocks.float_to_complex()

        # self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_char,
        #                                            1,
        #                                            socket_str,
        #                                            16,
        #                                            False,
        #                                            -1)

        self.zeromq_push_sink_test = zeromq.push_sink(gr.sizeof_char,
                                                   1,
                                                   socket_str,
                                                   128,
                                                   False,
                                                   -1)

        self.analog_sig_source_x_1 = analog.sig_source_c(self.dac_rate, analog.GR_SQR_WAVE, 100, 0.1, 0, 0)
        # self.blocks_add_const_vxx_0 = blocks.add_const_cc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        if (DEBUG == False) : # Real Time Execution
            # USRP blocks
            # self.u_source()
            # self.u_sink()

            # limesdr blocks
            self.lime_source()
            self.lime_sink()

            ######## Connections #########
            self.connect(self.source, self.matched_filter)
            self.connect(self.matched_filter, self.gate)

            self.connect(self.gate, self.tag_decoder)
            self.connect((self.tag_decoder,0), self.reader)
            self.connect((self.tag_decoder,1), (self.zeromq_push_sink_test, 0))
            self.connect(self.reader, self.amp)
            self.connect(self.amp, self.to_complex)
            self.connect(self.to_complex, (self.blocks_add_xx_0, 1))
            self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 0))

            # self.connect(self.to_complex, (self.blocks_add_const_vxx_0, 0))
            # self.connect((self.blocks_add_const_vxx_0, 0), (self.sink, 0))
            # self.connect((self.blocks_add_const_vxx_0, 0), self.file_sink_source)
            self.connect((self.blocks_add_xx_0, 0), (self.sink, 0))
            # self.connect((self.analog_sig_source_x_1, 0), self.file_sink_source)
            #File sinks for logging (Remove comments to log data)
            # self.connect(self.source, self.file_sink_source)

        else :  # Offline Data
            print("Use offline data.")
            self.file_source = blocks.file_source(gr.sizeof_gr_complex*1, cwd + os.sep + "../misc/data/file_source_test",False)   ## instead of uhd.usrp_source
            self.file_sink = blocks.file_sink(gr.sizeof_gr_complex*1,  cwd + os.sep + "../misc/data/file_sink", False)     ## instead of uhd.usrp_sink

            ######## Connections #########
            self.connect(self.file_source, self.matched_filter)
            self.connect(self.matched_filter, self.gate)
            # self.connect(self.matched_filter, (self.zeromq_push_sink_test, 0))
            self.connect(self.gate, self.tag_decoder)
            self.connect((self.tag_decoder,0), self.reader)
            self.connect((self.tag_decoder,1), (self.zeromq_push_sink_test, 0))

            # self.connect((self.tag_decoder,0), self.reader)
            self.connect(self.reader, self.amp)
            self.connect(self.amp, self.to_complex)
            self.connect(self.to_complex, self.file_sink)

            #File sinks for logging
            #self.connect(self.gate, self.file_sink_gate)
        # self.connect((self.tag_decoder,1), self.file_sink_decoder) # (Do not comment this line)

        # self.connect((self.tag_decoder,1), (self.zeromq_push_sink_0, 0))

        #self.connect(self.file_sink_reader, self.file_sink_reader)
        #self.connect(self.matched_filter, self.file_sink_matched_filter)

    # Configure usrp source
    def u_source(self):
        self.source = uhd.usrp_source(device_addr=self.usrp_address_source,
        stream_args=uhd.stream_args(cpu_format="fc32",channels=list(range(1)),
        ),
        )
        self.source.set_samp_rate(self.adc_rate)
        self.source.set_center_freq(self.freq, 0)
        self.source.set_gain(self.rx_gain, 0)
        self.source.set_antenna("RX2", 0)
        #self.source.set_auto_dc_offset(False) # Uncomment this line for SBX daughterboard

    # Configure lime u_source
    def lime_source(self):
        self.source = limesdr.source('', 0, '', False)
        self.source.set_sample_rate(self.adc_rate)
        self.source.set_center_freq(self.freq, 0)
        self.source.set_gain(self.rx_gain, 0)
        self.source.set_antenna(255, 0)

        self.source.set_bandwidth(self.rx_bw, 0)
        self.source.set_digital_filter(self.adc_rate, 0)
        self.source.calibrate(self.cal_bw , 0)

    # Configure usrp sink
    def u_sink(self):
        self.sink = uhd.usrp_sink(device_addr=self.usrp_address_sink,
        stream_args=uhd.stream_args(cpu_format="fc32",channels=list(range(1)),
        ),
        )
        self.sink.set_samp_rate(self.dac_rate)
        self.sink.set_center_freq(self.freq, 0)
        self.sink.set_gain(self.tx_gain, 0)
        self.sink.set_antenna("TX/RX", 0)

    # Configure lime sink
    def lime_sink(self):
        self.sink = limesdr.sink('', 0, '', '')
        self.sink.set_sample_rate(self.dac_rate)
        self.sink.set_center_freq(self.freq + self.freq_off, 0)
        self.sink.set_gain(self.tx_gain, 0)
        self.sink.set_antenna(255, 0)

        self.sink.set_bandwidth(self.tx_bw, 0)
        # self.sink.set_digital_filter(self.adc_rate, 0)
        self.sink.calibrate(self.cal_bw, 0)


if __name__ == '__main__':
    # print(f"Size of gnuradio float: {gr.sizeof_float}")
    # print(f"Size of gnuradio complex: {gr.sizeof_gr_complex}")
    # print(f"Size of gnuradio char: {gr.sizeof_char}")
    main_block = reader_top_block()
    main_block.start()
    
    pub = Publisher(ip="*", port="5556")

    # start the receiver socket
    zmq_consumer(pub)
    #
    while(1):
        inp = input("'Q' to quit \n")
        if (inp == "q" or inp == "Q"):
            break

    main_block.reader.print_results()
    main_block.stop()
