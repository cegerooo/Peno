#!/usr/bin/python3
#interactive-client.py

import socket
import telnetlib

def interact(socket):
    t = telnetlib.Telnet()
    t.socket = socket
    t.interact()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.63.68"
port = 2003

client.connect((host, port)) # Connect to our client
#while True:
msg = client.recv(1024)
#  if not msg:
#    break
print (msg.decode('ascii'))
interact(client)
client.close()
