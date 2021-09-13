#!/usr/bin/env python3

import socket

# The port that we want to bind to our server
PORT = 5050
# IP address of the server
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# Specification of my own custom protocol
HEADER_SIZE = 64
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# create an INET, STREAMing socket (TCP/IP)
# AF_INET: Address Family of Internet Protocol v4
# SOCK_STREAM:  TCP Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to a remote socket at address
# Note: TCP is a connection-oriented protocol
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    msgHeader = str(msgLength).encode(FORMAT)
    # Pad spaces to the msgHeader in order to fill the HEADER
    msgHeader += b' ' * (HEADER_SIZE - len(msgHeader))
    # Send the msgHeader
    client.send(msgHeader)
    # Send the main message
    client.send(message)

send("Hello World!")