"""
Given a string s, your task is to print to the standard output 
(stdout) the number of digits it contains.
"""

def count_digits(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    dig = '1234567890'
    print len([num for num in s if num in dig])