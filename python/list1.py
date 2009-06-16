#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""docstring
"""

__revision__ = '0.1'

import stat, sys, os, string, commands

try:
    #run a 'find' command and assign results to a variable 
    pattern = raw_input("Enter the file pattern to search for:\n")
    commandString = "find " + patterncommandOutput = commands.getoutput(commandString)
    findResults = string.split(commandOutput, "\n")

    #output find results, along with permissions
    print "Files:"
    print commandOutput
    print "=" * 30
    for file in findResults:
        mode = stat.S_IMODE(os.listat(file)[stat.ST_MODE])
        print '\nPerminssions for file ', file, ':'
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode %amp; getattr(stat, "S_I"+perm+level):
                    print leve, " has ", perm, " permissions"
                else:
                    print level, " does NOT have ", perm, " permissions"
except:
    print "There was a problem - check the message above"

