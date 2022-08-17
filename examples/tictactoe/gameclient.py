#!/usr/bin/env python3

import socket as sock

def initializeClient(name):
    HOST = '192.168.1.170'
    PORT = 8080
    with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = '{}: hello server'.format(name)
        s.send(bytes(msg, 'utf-8'))
        data = s.recv(1024)
    print("received: {}".format(data))

initializeClient('player1')