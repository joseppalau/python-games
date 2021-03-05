import socket
import pickle

class Network:
	def __init__(self, server, port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = server
		self.port = port
		self.addr = (self.server, self.port)
		self.pos = self.connect()

	def get_pos(self):
		return self.pos	

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))
		except:
			print('error al conectar')		

	def sending(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))	
		except:
			print('error al enviar')		
