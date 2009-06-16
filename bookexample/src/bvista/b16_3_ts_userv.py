#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2009-5-17

'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_ser_sock = socket(AF_INET, SOCK_DGRAM)
udp_ser_sock.bind(ADDR)

while True:
    print 'waiting for message ...'
    data, addr = udp_ser_sock.recvfrom(BUFSIZ)
    udp_ser_sock.sendto('[%s] %s' % (ctime( ), data), addr)
    print '...received from and return to:', addr
    
udp_ser_sock.close()