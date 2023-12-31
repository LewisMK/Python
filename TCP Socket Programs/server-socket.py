#!/usr/bin/python

import socket

s = socket.socket()             # create a socket object. note that we do not have to specify the family and type if we are using TCP sockets.
host = socket.gethostname()     # get current machine name (not its IP)
port = 9999                     # get port number for connection


s.bind((host, port))            # bind host with the port

print ("Waiting for connection...")

s.listen(5)                     # listen for connections

while True:
    
    conn, addr = s.accept()     # connect and accept from client
    
    print("Got connection from:", addr)
    
    
    message = "Server says Hi there!"
    
    conn.send(message.encode())
    
    conn.close()                # close the connection


# note that the server will continue listening for other connections after this one has been closed. 
    
    
