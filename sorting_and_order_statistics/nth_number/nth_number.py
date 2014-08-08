"""
Given an array of unsorted but unique integers, 
your task is to print the n-th largest value.

"""
def nth_number(v, n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    print sorted(v)[-n]
