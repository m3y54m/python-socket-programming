#!/usr/bin/env python3

import socket

# UDP destination (server) spec
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "Hello, Server"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
