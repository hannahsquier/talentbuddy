"""
Given 2 sorted arrays, merge them into one single sorted 
array and print its elements to standard output.

"""

def merge_arrays(a, b):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    for e in b:
        a.append(e)
    for i in sorted(a):
        print i

