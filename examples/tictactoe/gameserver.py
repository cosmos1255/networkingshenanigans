#!/usr/bin/env python3

import socket as sock

def initializeServer():
    HOST = ''
    PORT = 8080
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(2)
        conn, addr = s.accept()
        with conn:
            print('Connected: ', addr)
            while True:
                data = conn.recv(1024)
                print(data)
                conn.send(b"msg received")