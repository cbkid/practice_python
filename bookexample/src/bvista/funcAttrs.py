#!/usr/bin/env python

'''
Created on 2009-5-16

'''
def foo():
    return True

def bar():
    'bar() does not do much'
    return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print 'PASSED'
else:
    print 'FAILED'
    '''
    
for each_attr in dir():
    obj = eval(each_attr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print '\nFunction "%s" has a doc string:\n\t%s' % (each_attr, obj.__doc__)
            if hasattr(obj, 'tester'):
                print 'Function "%s" has tester... executing' % each_attr
                exec obj.tester
            else:
                print 'Function "%s" has no tester... skipping' % each_attr
    else:
        print '"%s" is not a function' % each_attr
                