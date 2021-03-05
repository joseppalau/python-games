import socket
import _thread as th
import sys
from client import read_pos, make_pos
from player import Player
import pickle

server = input('Introduce IP').strip()
port = int(input('Introduce Port').strip())
players = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))

except socket.error as e:
		print('some error')
		str(e)

else:
	s.listen(2)
	players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]
	print('Wating for a connection, Server Started')

pos = [(0,0), (100,100)]	

def threaded_client(conn, player):
	conn.send(pickle.dumps(players[player]))
	reply = ''
	while True:
		try:
			data = pickle.loads(conn.recv(2048))
			players[player] = data
		
		except:
			print('Non data. Disconnected')
			break

		else:
			if player == 1:
				reply = players[0]
			else:
				reply = players[1]	
			#print('Recieved: ', reply)	
			#print('Sending: ', reply)
			conn.sendall(pickle.dumps(reply))	

	print('Lost connection')	
	conn.close()	

currentPlayer = 0

while True:
	conn, addr = s.accept()
	print('Connected to:', addr)

	th.start_new_thread(threaded_client,(conn,currentPlayer))
	currentPlayer += 1	

