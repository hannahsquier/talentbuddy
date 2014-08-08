"""
Create a function that takes an input string and encrypts it using a caesar shift of +1.
Please print the shifted string to the standard output (stdout)
"""
def caesar_shift(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    old = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
    
    for  l in s:
        if l != 'Z' and l != ' ':
            s = s.replace(l, new[old.find(l)])
        if l == 'Z':
            s = s.replace(l, 'A')
        
    print s