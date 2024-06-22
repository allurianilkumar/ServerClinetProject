#import socket module
from socket import *
import time
import logging
log = logging.getLogger("my-logger")

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
print(socket.hostname())
serverPort = 7001
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
log.info("listening Server...")
#Fill in end
requestedCounts=0
while True:
	#Establish the connection
	print('Ready to serve...')
	# connectionSocket, addr = #Fill in start #Fill in end
	t1 = time.time()
	connectionSocket, addr = serverSocket.accept()
	print("Connection from: " + str(addr))
	try:
		message = connectionSocket.recv(1024)
		print(message)
		if len(message) != 0:
			# is received
			t2 = time.time()
			requestedCounts=requestedCounts+1;
			filename = message.split()[1]
			f = open(filename[1:])
			outputdata = f.read()
			#Send one HTTP header line into socket
			#Fill in start
			connectionSocket.send(b"HTTP/1.1 201 OK\r\n\r\n")
			#Fill in end
			print(outputdata)
			connectionSocket.send(outputdata.encode('utf-8'))
			connectionSocket.send(b"\r\n\r\nConnection Counts="+str(requestedCounts).encode('utf-8'))
			#Send the content of the requested file to the client
			# for i in range(0, len(outputdata)):
			# 	connectionSocket.send(outputdata[i].encode('utf-8'))
			# total time taken
			tim = str(t2-t1)
			connectionSocket.send(b"\r\n\r\nRound Trip Time="+str(tim).encode('utf-8'))
			connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start
		# connectionSocket.send('\n404 File Not Found\n')
		# is received
		t2 = time.time()
		connectionSocket.send(b"HTTP/1.1 404 Not found\r\n\r\n")
		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.send(b"<html><head></head><body><h1>404 Not found</h1></body></html>\r\n")
		#Fill in end
		tim = str(t2-t1)
		connectionSocket.send(b"\r\n\r\nRound Trip Time="+str(tim).encode('utf-8'))
		connectionSocket.close()
serverSocket.close()
