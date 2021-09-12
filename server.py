#!/usr/bin/env python3

import socket
import threading

PORT = 5050
# IP address of your computer
# SERVER = "192.168.1.104"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# create an INET, STREAMing socket (TCP/IP)
# AF_INET: Address Family of Internet Protocol v4
# SOCK_STREAM:  TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to address
server.bind(ADDR)
