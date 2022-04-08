import zmq
import random
import sys
import time


class Publisher:
	def __init__(self, ip="127.0.0.1", port="5556"):
		self.port = port
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.PUB)
		self.socket.bind(f"tcp://{ip}:{port}")

	def publish(self, epc_0x_str, rssi_str, time_delay_s):
		print("published.")
		self.socket.send_multipart([bytes(epc_0x_str, 'utf-8'), bytes(rssi_str, 'utf-8')])
		time.sleep(time_delay_s)


if __name__ == "__main__":
	pub = Publisher()
	while True:
		EPC = random.choice(['e45684a6845d84568f568456', '912391fa9123ec239123912b'])
		RSSI = str(round(random.uniform(-35,-50), 3))
		pub.publish(epc_0x_str=EPC, rssi_str=RSSI, time_delay_s=1)
