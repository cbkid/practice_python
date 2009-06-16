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

udp_cli_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udp_cli_sock.sendto(data, ADDR)
    data, ADDR = udp_cli_sock.recvfrom(BUFSIZ)
    if not data:
        break
    print data
    
    udp_cli_sock.close()