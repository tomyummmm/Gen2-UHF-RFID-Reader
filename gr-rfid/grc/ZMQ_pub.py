from __future__ import unicode_literals
import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
	port = sys.argv[1]
	int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:%s" % port)

while True:
	EPC = '912391239123912391239123'
	RSSI = '-48.8'
	socket.send_multipart([bytes(EPC, 'utf-8'), bytes(RSSI, 'utf-8')])
	print('Sent')
	time.sleep(3)
