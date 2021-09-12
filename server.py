#!/usr/bin/env python3

import socket
import threading

PORT = 5050
# IP address of your computer
#SERVER = "192.168.1.104"
SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)
