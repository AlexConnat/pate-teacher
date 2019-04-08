#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 4:
    print("Usage: %s server_ip server_port prediction_file" % (sys.argv[0])) # MUST BE A VALID IP AND VALID PORT
    exit(1)

CHUNK_SIZE = 8 * 1024
SERVER_IP = sys.argv[1]          # "10.10.55.100"
SERVER_PORT = int(sys.argv[2])   # 1337

sock = socket.socket()
sock.connect( (SERVER_IP, SERVER_PORT) )

print("[*] Connected to " + SERVER_IP + "\n")

#filename = "checkpoints/predictions.npy"
filename = sys.argv[3]
with open(filename, "rb") as f:
	
    data = f.read(CHUNK_SIZE)
    while data:
        sock.send(data)
        data = f.read(CHUNK_SIZE)
	
    print("Sent predictions!\n")
    
    sock.close()
