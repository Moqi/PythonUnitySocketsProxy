import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
try:
	#Bind the socket to a port
    s.bind((HOST, PORT))
except (socket.error , msg):
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')

s.listen(10)
print('Socket listening on port: 8888')
while 1:
	conn, addr = s.accept()
	print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	data = conn.recv(1024)
	if not data:
		break
	else:
		reply = 'OK...' + data.decode(encoding='UTF-8')
		conn.sendall(reply.encode('ascii'))
 
conn.close()
s.close()