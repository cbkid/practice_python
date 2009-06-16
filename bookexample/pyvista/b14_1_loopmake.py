#!/usr/bin/env python

dashes = '\n' + '-' * 50 #dashes line
exec_dict = {
             'f' : """ #for loop
             for %s in %s:
                 print %s
                 """,
             'n' : """ # counting while loop
             %s = %d
             while %s < %d:
                 print %s
                 %s = %s + %d
                 """,
              's' : """ # sequence while loop
                 %s = 0
                 %s = %s
                 while %s < len(%s):
                     print %s[%s]
                     %s = %s + 1
                     """
                         }
def main():
    
    ltype = raw_input('Loop type? (For/While)')
    dtype = raw_input('Data type? (Number/Seq)')
    
    if dtype == 'n':
        start = input('Staring value?')
        stop = input('Ending value (non-inclusive)?')
        step = input('Stepping value?')
        seq = str(range(start, stop, step))
        
    else:
        seq = raw_input('Enter sequence:')
        
    var = raw_input('Iterative variable name?')
        
    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)
            
    elif ltype == 'w':
	    if dtype == 's':
	        svar = raw_input('Enter sequence name?')
	        exec_str = exec_dict['s'] % \
	        (var, svar, seq, var, svar, svar, var, var, var)
	    elif dtype == 'n':
	        exec_str = exec_dict['n'] % \
	        (var, start, var, stop, var, var, var, step)
	                
    print dashes
    print 'Your custom-generated code:' + dashes
    print exec_str + dashes
    print 'Test excution of the code:' + dashes
    exec exec_str
    print dashes
        
if __name__ == '__main__':
    main()
    
    
#some indent errorZZ