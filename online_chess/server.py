import socket
import _thread as th
import sys

server = '192.168.1.132'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))

except socket.error as e:
		print('some error')
		str(e)

else:
	s.listen(2)
	print('Wating for a connection, Server Started')

def threaded_client(conn):
	conn.send(str.encode('Connected'))
	reply = ''
	while True:
		try:
			data = conn.recv(2048)
			reply = data.decode('utf-8')
		
		except:
			print('Non data. Disconnected')
			break

		else:
			#print('Recieved: ', reply)	
			#print('Sending: ', reply)
			conn.sendall(str.encode(reply))	

	print('Lost connection')	
	conn.close()	


while True:
	conn, addr = s.accept()
	print('Connected to:', addr)

	th.start_new_thread(threaded_client(conn), (conn,))

