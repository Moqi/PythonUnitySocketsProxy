
# Creating a socket client. This is synonymous to the Game on iPad
import socket
#AF_INET: Address Family : AF_INET (this is IP version 4 or IPv4)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
	print("Socket creation failed. Error code: " +str(msg[0])+" , Error message: " + msg[1])
	s.close()
	sys.exit()
	
print("The client has successfully created a socket")

#Connect to the target. 
host = "www.google.com"
port =80

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	s.close()
	sys.exit()

print("IP Address of " + host + " is: " + str(remote_ip))

#Connect to the server
try:
	s.connect((remote_ip, port))
except socket.error:
	print("Connection to the server failed")
	s.close()
	sys.exit()

print("Connected to the server")

#Send data to the server
message = "GET / HTTP/1.1\r\n\r\n"
try:
	#Send the message
	s.sendall(message.encode('ascii'))
except socket.error:
	#Failed to send the request message
	print ("Request resulted in an error")
	s.close()
	sys.exit()
	
print("Request submitted to server")

#Handling the response
response = s.recv(4096)
print("The response from the server:\n")
print(response)

s.close()