#!/usr/bin/python

import socket

s = socket.socket()

host = socket.gethostname()  # this command will get the host name where this script is running from

port = 9999

s.connect((host, port))

print(s.recv(1024))

s.close()