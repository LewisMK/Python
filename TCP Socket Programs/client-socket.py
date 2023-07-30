#!/usr/bin/python

import socket

s = socket.socket()

host = socket.gethostname()  # this command will get the host name where this script is running from

port = 9999                   # the target port has to match the server's listening port

s.connect((host, port))

print(s.recv(1024))          # 1024 bytes is the TCP maximum message size (MSS). It is usually 1460 bytes after removing TCP and IP header length from the MTU

s.close()
