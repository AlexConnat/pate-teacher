#!/usr/bin/python

import socket

CHUNK_SIZE = 8 * 1024
SERVER_IP = "10.10.55.100"
SERVER_PORT = 1337

sock = socket.socket()
sock.connect( (SERVER_IP, SERVER_PORT) )

print("[*] Connected to " + SERVER_IP + "\n")

filename = "checkpoints/predictions.npy"
with open(filename, "rb") as f:
	
	data = f.read(CHUNK_SIZE)
	while data:
		sock.send(data)
	    	data = f.read(CHUNK_SIZE)
	
	print("Sent data!\n")

	sock.close()
