"""
Given an array of integer numbers your task is 
to print to the standard output (stdout) the majority number.

"""

def majority(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    
    for e in v:
        if v.count(e) > len(v)/2:
            print e
            return
        
    print None