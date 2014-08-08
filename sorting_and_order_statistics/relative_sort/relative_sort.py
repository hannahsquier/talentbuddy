"""
Given an array of integer numbers your task is to print to the 
standard output (stdout) the initial array, but sorted in a special 
way:

all negative numbers come first and their relative positions according to the initial array do not change

the same with the positive integers, but they come last

"""

def relative_sort(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    vector = [x for x in v if x <= 0] + [x for x in v if x >= 0]
    for e in vector: print e,