"""
Given two percentages p1, p2 and an integer number v your task 
is to print to the standard output two integer numbers, the first 
one representing p1 percent from v and the second one p2 percent 
from v. The two percentage numbers will always add up to 1.

If rounding is necessary, round the first number half up 
(.5 and up goes to 1) and ensure total of calculated values is 
total given value v originally.
"""

def precision(p1, p2, v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    import math
    int1 = int(round(p1*v))
    int2 = v - int1
    print int1, int2
