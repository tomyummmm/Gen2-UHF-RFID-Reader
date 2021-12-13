#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
from gnuradio import qtgui

# data transfer lib
from gnuradio import blocks
from gnuradio import zeromq
import array
import zmq
socket_str = "tcp://127.0.0.1:5557"

# data plot lib
import cv2
import numpy as np


# data plot code
# Plot values in opencv program
class Plotter:
    def __init__(self, plot_width, plot_height, scale_factor=100, cont=True):
        self.width = plot_width
        self.height = plot_height
        self.color = (255, 0, 0)
        self.val = []
        self.plot = np.ones((self.height, self.width, 3)) * 255
        self.scale = scale_factor
        self.cont = cont
        cv2.line(self.plot, (0, int(self.height / 2)), (int(self.width), int(self.height / 2)), (0, 255, 0), 1)
        print("Plotter is initialized...")

    # Update new values in plot
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

    # Show plot using opencv imshow
    def show_plot(self, label):
        for i in range(len(self.val)-1):
            cv2.line(self.plot, (i, int(self.height/2) - self.val[i]), (i+1, int(self.height/2) - self.val[i+1]), self.color, 1)
        cv2.imshow(label, self.plot)
        cv2.waitKey(1)


# data transfer code
def zmq_consumer():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.connect(socket_str)
    p = Plotter(1024, 400, scale_factor=8000, cont=False)
    while True:
        # pull in raw binary data
        raw_data = results_receiver.recv()
        # convert to an array of floats
        float_list = array.array('f', raw_data)  # struct.unpack will be faster
        # print flowgraph data

        for signal_val in float_list:
            # print(signal_val)
            p.update(signal_val)


class car_remote(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "car_remote")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'qt_gui_freq_1', #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        self.blocks_throttle_0 = blocks.throttle(
            gr.sizeof_float * 1,
            samp_rate,
            True)
        # print(gr.sizeof_float)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float * 2,
                                                   1,
                                                   socket_str,
                                                   100,
                                                   False,
                                                   -1)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'driver=lime,soapy=0'
        )
        self.osmosdr_source_0.set_clock_source('internal', 0)
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(434e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('LNAL', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)



        ##################################################
        # Connections
        ##################################################
        # self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        # self.connect((self.osmosdr_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.zeromq_push_sink_0, 0))
        # self.connect((self.qtgui_freq_sink_x_0, 0), (self.zeromq_push_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "car_remote")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)



def main(top_block_cls=car_remote, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    # start the receiver socket
    zmq_consumer()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
