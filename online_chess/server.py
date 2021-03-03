import socket
import _thread as th
import sys
from client import read_pos, make_pos

server = input('Introduce IP').strip()
port = int(input('Introduce Port').strip())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))

except socket.error as e:
		print('some error')
		str(e)

else:
	s.listen(2)
	print('Wating for a connection, Server Started')

pos = [(0,0), (100,100)]	

def threaded_client(conn, player):
	conn.send(str.encode(make_pos(pos[player])))
	reply = ''
	while True:
		try:
			data = read_pos(conn.recv(2048).decode())
			pos[player] = data
		
		except:
			print('Non data. Disconnected')
			break

		else:
			if player == 1:
				reply = pos[0]
			else:
				reply = pos[1]	
			#print('Recieved: ', reply)	
			#print('Sending: ', reply)
			conn.sendall(str.encode(make_pos(reply)))	

	print('Lost connection')	
	conn.close()	

currentPlayer = 0

while True:
	conn, addr = s.accept()
	print('Connected to:', addr)

	th.start_new_thread(threaded_client,(conn,currentPlayer))
	currentPlayer += 1	

