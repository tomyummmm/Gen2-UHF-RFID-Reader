#Developed by: Nikos Kargas 

from gnuradio import eng_notation
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from gnuradio.eng_arg import eng_float, intx
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio import gr
from gnuradio import uhd
from gnuradio import blocks
from gnuradio import filter
from gnuradio import analog
from gnuradio import digital
from gnuradio import qtgui
from gnuradio import zeromq
from time import sleep
import rfid
import sip
import sys
import signal
import time
import array
import zmq

socket_str = "tcp://127.0.0.1:5557"

import cv2
import numpy as np

class Plotter:
    def __init__(self, plot_width, plot_height, scale_factor=100, cont=True):
        self.width = plot_width
        self.height = plot_height
        self.color = (255, 0, 0)
        self.val = []
        self.plot = np.ones((self.height, self.width, 3)) * 255
        self.scale = scale_factor
        self.cont =cont
        cv2.line(self.plot, (0, int(self.height / 2)), (int(self.width), int(self.height / 2)), (0, 255, 0), 1)
    
    def update(self, val, label="plot"):
        self.val.append(int(val * self.scale))
        while len(self.val) > self.width:
            self.plot = np.ones((self.height, self.width, 3)) * 255
            if self.cont:
                self.val.pop(0)
            else:
                self.val = self.val[-1:]
        if len(self.val) == self.width:
            self.show_plot(label)
    
    def show_plot(self, label):
        for i in range(len(self.val)-1):
            cv2.line(self.plot, (i, int(self.height/2) - self.val[i]), (i+1, int(self.height/2) - self.val[i+1]), self.color, 1)
        cv2.imshow(label, self.plot)
        cv2.waitKey(1)

def zmq_consumer():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.connect(socket_str)
    p = Plotter(1024, 400, scale_factor=8000, cont=False)
    while True:
        raw_data = results_receiver.recv()
        float_list = array.array('f', raw_data)

        for signal_val in float_list:
            p.update(signal_val)

DEBUG = True

class reader_top_block(gr.top_block):

  # Configure usrp source
  def u_source(self):
    self.source = uhd.usrp_source(
    device_addr=self.usrp_address_source,
    stream_args=uhd.stream_args(
    cpu_format="fc32",
    channels=range(1),
    ),
    )
    self.source.set_samp_rate(self.adc_rate)
    self.source.set_center_freq(self.freq, 0)
    self.source.set_gain(self.rx_gain, 0)
    self.source.set_antenna("RX2", 0)
    #self.source.set_auto_dc_offset(False) # Uncomment this line for SBX daughterboard

  # Configure usrp sink
  def u_sink(self):
    self.sink = uhd.usrp_sink(
    device_addr=self.usrp_address_sink,
    stream_args=uhd.stream_args(
    cpu_format="fc32",
    channels=range(1),
    ),
    )
    self.sink.set_samp_rate(self.dac_rate)
    self.sink.set_center_freq(self.freq, 0)
    self.sink.set_gain(self.tx_gain, 0)
    self.sink.set_antenna("TX/RX", 0)
    
  def __init__(self):
    gr.top_block.__init__(self)


    #rt = gr.enable_realtime_scheduling() 

    ######## Variables #########
    self.dac_rate = 1e6                 # DAC rate 
    self.adc_rate = 100e6/50            # ADC rate (2MS/s complex samples)
    self.decim     = 5                    # Decimation (downsampling factor)
    self.ampl     = 0.1                  # Output signal amplitude (signal power vary for different RFX900 cards)
    self.freq     = 910e6                # Modulation frequency (can be set between 902-920)
    self.rx_gain   = 20                   # RX Gain (gain at receiver)
    self.tx_gain   = 0                    # RFX900 no Tx gain option

    self.usrp_address_source = "addr=192.168.10.2,recv_frame_size=256"
    self.usrp_address_sink   = "addr=192.168.10.2,recv_frame_size=256"

    # Each FM0 symbol consists of ADC_RATE/BLF samples (2e6/40e3 = 50 samples)
    # 10 samples per symbol after matched filtering and decimation
    self.num_taps     = [1] * 25 # matched to half symbol period

    ######## File sinks for debugging (1 for each block) #########
    self.file_sink_source         = blocks.file_sink(gr.sizeof_gr_complex*1, "../misc/data/source", False)
    self.file_sink_sink           = blocks.file_sink(gr.sizeof_gr_complex*1, "../misc/data/sink", False)
    self.file_sink_matched_filter = blocks.file_sink(gr.sizeof_gr_complex*1, "../misc/data/matched_filter", False)
    self.file_sink_gate           = blocks.file_sink(gr.sizeof_gr_complex*1, "../misc/data/gate", False)
    self.file_sink_decoder        = blocks.file_sink(gr.sizeof_float*1, "../misc/data/decoder", False)
    self.file_sink_reader         = blocks.file_sink(gr.sizeof_float*1,      "../misc/data/reader", False)

    ######## Blocks #########
    self.matched_filter = filter.fir_filter_ccc(self.decim, self.num_taps);
    self.gate            = rfid.gate(int(self.adc_rate/self.decim))
    self.tag_decoder    = rfid.tag_decoder(int(self.adc_rate/self.decim))
    self.reader          = rfid.reader(int(self.adc_rate/self.decim),int(self.dac_rate))
    self.amp              = blocks.multiply_const_ff(self.ampl)
    self.to_complex      = blocks.float_to_complex()

    #self.zeromq_push_sink = zeromq.push_sink(gr.sizeof_gr_complex, 1, socket_str, 100, False, -1)
    self.zeromq_pub_sink = zeromq.pub_sink(gr.sizeof_float, 1, socket_str, 100, False, -1)

    if (DEBUG == False) : # Real Time Execution

      # USRP blocks
      self.u_source()
      self.u_sink()

      ######## Connections #########
      self.connect(self.source,  self.matched_filter)
      self.connect(self.matched_filter, self.gate)

      self.connect(self.gate, self.tag_decoder)
      self.connect((self.tag_decoder,0), self.reader)
      self.connect(self.reader, self.amp)
      self.connect(self.amp, self.to_complex)
      self.connect(self.to_complex, self.sink)

      self.connect(self.source, self.zeromq_push_sink)

      #File sinks for logging (Remove comments to log data)
      self.connect(self.source, self.file_sink_source)
      self.connect(self.to_complex, self.file_sink_sink)

    else :  # Offline Data
      self.file_source               = blocks.file_source(gr.sizeof_gr_complex*1, "../misc/data/file_source_test",False)   ## instead of uhd.usrp_source
      self.file_sink                  = blocks.file_sink(gr.sizeof_gr_complex*1,   "../misc/data/file_sink", False)     ## instead of uhd.usrp_sink
 
      ######## Connections ######### 
      self.connect(self.file_source, self.matched_filter)
      self.connect(self.matched_filter, self.gate)
      self.connect(self.gate, self.tag_decoder)
      self.connect((self.tag_decoder,0), self.reader)
      self.connect(self.reader, self.amp)
      self.connect(self.amp, self.to_complex)
      self.connect(self.to_complex, self.file_sink)
    
    #File sinks for logging 
    #self.connect(self.gate, self.file_sink_gate)
    self.connect((self.tag_decoder,1), self.file_sink_decoder) # (Do not comment this line)
    #self.connect(self.file_sink_reader, self.file_sink_reader)
    #self.connect(self.matched_filter, self.file_sink_matched_filter)
    #self.connect((self.tag_decoder,1), self.zeromq_pub_sink)

if __name__ == '__main__':
    main_block = reader_top_block()
    main_block.start()

    while(1): 
        inp = input("'Q' to quit \n")
        if (inp == "q" or inp == "Q"):
            break

    main_block.reader.print_results()
    main_block.stop()

