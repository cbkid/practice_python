#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2009-5-17

'''

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
tcp_cli_sock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcp_cli_sock.send(data)
    data = tcp_cli_sock.recv(BUFSIZ)
    if not data:
        break
    print data
    
tcp_cli_sock.close()