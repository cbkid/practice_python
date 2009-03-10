#!/usr/bin/env python

import keyword
import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')
inp = input('Identifier to test?')

if  not keyword.iskeyword(inp):
    if len(inp) >= 1:
            if inp[0] not in alphas:
                    print('''invalid: first symbol must be alphabetic''')
            else:
                    alphnus = alphas + nums
                    for other_char in inp[1:]:
                            if other_char not in alphnus :
                                    print('''invalid: remaining symbols must be alphanumeric ''')
                                    break
                    else:
                            print("okay as an identifier")

