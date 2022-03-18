import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Connecting to IP Address')
# Connect is for remote ip address of PUB server
socket.connect("tcp://127.0.0.2:5556")
# socket.connect("tcp://192.168.1.119:5556")
# socket.connect("tcp://192.168.1.103:5000")

# Subscribe to topic
socket.setsockopt(zmq.SUBSCRIBE, b'')  # subscribe to topic of all

running = True

while running:
	EPC, RSSI = socket.recv_multipart()
	print(EPC, RSSI)
	EPC = EPC.decode('utf-8')
	RSSI = float(RSSI.decode('utf-8'))
	print(EPC, RSSI)
