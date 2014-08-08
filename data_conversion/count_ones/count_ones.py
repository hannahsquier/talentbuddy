"""
write a function that prints to the standard output (stdout) 
the number of 1's present in its binary representation

"""

def count_one(a):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"

    print bin(a)[2:].count('1')