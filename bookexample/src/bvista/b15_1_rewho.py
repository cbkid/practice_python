#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2009-5-17

'''

from os import popen
from re import split

f = popen('dir','r')
for each_line in f.readlines():
    print split('\s\s+|\t', each_line.strip())
f.close()