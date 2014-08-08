"""
Print to the standard output (stdout) the sum of all the 
odd numbers squared between x and y.
y will always be greater than x.

"""

def odd_square_sum(x, y):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    print sum([x**2 for x in range(x,y+1) if x % 2 != 0])