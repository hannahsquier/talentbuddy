"""
Given an integer number N, compute its square root 
without using any math library functions and print 
the result to standard output. Please round the result 
downwards to the nearest integer (e.g both 7.1 and 7.9 are rounded to 7)

"""

def compute_sqrt(n):

    for i in range(0, n):
        if i * i <= n:
            continue
        else:
            sqrt = i-1
            break
    print sqrt