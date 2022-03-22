from __future__ import unicode_literals
import zmq
import random
import sys
import time
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0)
try:
	# doesn't even have to be reachable
	s.connect(('10.255.255.255', 1))
	IP = s.getsockname()[0]
except Exception:
	IP = '127.0.0.1'
finally:
	s.close()

port = "5556"
if len(sys.argv) > 1:
	port = sys.argv[1]
	int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
# socket.bind("tcp://127.0.0.2:%s" % port)
# Bind is for local endpoint, * or localhost. Not specific IP?
# socket.bind("tcp://*:%s" % port)
socket.bind("tcp://" + str(IP) + ":%s" % port)
print("Binding to tcp://" + str(IP) + ":%s" % port)

while True:
	# EPC = '912391239123912391239123'
	EPC = random.choice(['845684568456845684568456', '912391239123912391239123'])
	RSSI = str(round(random.uniform(-35, -50), 3))
	socket.send_multipart([bytes(EPC, 'utf-8'), bytes(RSSI, 'utf-8')])
	print('Sent')
	time.sleep(0.01)
