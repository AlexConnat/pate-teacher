#!/usr/bin/python

import socket

CHUNK_SIZE = 8 * 1024
SERVER_IP = "129.132.167.122"
SERVER_PORT = 1337

sock = socket.socket()
sock.connect( (SERVER_IP, SERVER_PORT) )

print("[*] Connected to " + SERVER_IP + "\n")

filename = "mnist_10_teachers_0.ckpt-2999.data-00000-of-00001"
with open(filename, "rb") as f:
	
	data = f.read(CHUNK_SIZE)
	while data:
		sock.send(data)
	    	data = f.read(CHUNK_SIZE)
	
	print("Sent data!\n")

	sock.close()
