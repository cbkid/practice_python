#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2009-5-18

'''

import thread
from time import sleep, ctime

def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 at:', ctime( )
    
def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime( )
    
def main():
    print 'starting at:', ctime( )
    thread.start_new(loop0, ())
    thread.start_new(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime( )
    
if __name__ == '__main__':
    main()