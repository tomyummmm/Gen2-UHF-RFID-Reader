import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)

print('Connecting to IP Address')
socket.connect("tcp://127.0.0.1:5556")

# Subscribe to topic
socket.setsockopt(zmq.SUBSCRIBE, b'')  # subscribe to topic of all

running = True

while running:
	EPC, RSSI = socket.recv_multipart()
	print(EPC, RSSI)
