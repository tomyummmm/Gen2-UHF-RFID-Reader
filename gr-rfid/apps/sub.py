import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5557')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    message = socket.recv()
    print(message)
