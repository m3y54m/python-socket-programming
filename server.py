#!/usr/bin/env python3

import socket
import threading

# The port that we want to bind to our server
PORT = 5050
# IP address of your computer
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# Specification of my own custom protocol
HEADER_SIZE = 64
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# create an INET, STREAMing socket (TCP/IP)
# AF_INET: Address Family of Internet Protocol v4
# SOCK_STREAM:  TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to address
server.bind(ADDR)


def handle_client(conn, addr):
    isConnected = True
    print(f"[NEW CONNECTION] {addr} connected.")
    # Keep receiving messages until the DISCONNECT_MSG arrives
    while isConnected:
        # First receive the size of incoming message
        msgLength = conn.recv(HEADER_SIZE).decode(FORMAT)

        # if msgLength != empty string
        if msgLength != "":
            msgLength = int(msgLength)
            print(f"[MESSAGE LENGTH] {msgLength}")
            # No receive the main message according to the size received before
            msg = conn.recv(msgLength).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                isConnected = False

            print(f"[{addr}] {msg}")

    # Close the client's socket connection
    conn.close()


def start():
    # Enable the server to accept connections
    # Note: TCP is a connection-oriented protocol
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:
        # Wait for a new connection to the server
        # conn: Connection to the client used for responding
        # addr: Address of the client
        conn, addr = server.accept()
        # Create a separate thread for handling the new client connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Number of clients equals number of threads created for clients minus the main thread
        clientsCount = threading.active_count() - 1
        print(f"[ACTIVE CLIENT CONNECTIONS] {clientsCount}")


print("[STARTING] server is starting ...")
start()
