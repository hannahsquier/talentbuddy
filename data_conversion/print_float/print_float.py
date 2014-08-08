"""
Given a binary string containing a fractional part your task 
is to print to the standard output (stdout) its numeric value (as a float).
"""

def print_float(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"

    num = int(s[:s.find('.')], 2)
    dec = s[s.find('.') + 1:]
    denom = 2 ** len(dec)
    numer = int(dec, 2)
  
    fract = float(numer) / denom
    
    print num + fract

