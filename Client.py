from socket import *
import sys
import time
import logging
log = logging.getLogger("my-logger")


clientsocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print(len(sys.argv))
    print("USE : Client.py server_host server_port filename")
    sys.exit(0)

host = str(sys.argv[1])
port = int(sys.argv[2])
request = str(sys.argv[3])
request = "GET /" + request + " HTTP/1.1"
try:
	t1 = time.time()
	clientsocket.connect((host,port))
except Exception as data:
    print(Exception,":",data)
    print("Please try again.\r\n")
    sys.exit(0)
clientsocket.send(request.encode('utf-8'))
t2 = time.time()
response = clientsocket.recv(1024).decode()
print(response)
if "201" in response:
	response1 = clientsocket.recv(1024).decode()
	tim = str(t2-t1)
	print("\nRound Trip Time="+str(tim))
	print(response1)
if "404" in response:
	t2 = time.time()
	print("Page Not Found")
	tim = str(t2-t1)
	print("\nRound Trip Time="+str(tim))
clientsocket.close()
