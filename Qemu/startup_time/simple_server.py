#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# host = socket.gethostname()                           
host = '0.0.0.0'

port = 26666                                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           


# establish a connection
clientsocket,addr = serversocket.accept()      

print("Got a connection from %s" % str(addr))

msg = 'Thank you for connecting'+ "\r\n"
clientsocket.send(msg.encode('ascii'))
clientsocket.close()