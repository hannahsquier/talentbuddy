"""Given a rational, decimal value, write a function prints 
out the simplest possible fraction.
The decimal value is given as a string value."""

def compute_fraction(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    

    dec = float(s) % 1
    whole = int(float(s))
    denom = 10**(int(dec/10)+1)
    num = int(denom * dec + denom * whole)
    
    for i in range(1, max(num,denom)):
        if num % i == 0 and denom % i == 0:
            num = num / i 
            denom = denom / i
    
    print str(num) + '/' + str(denom)