"""
Given an integer representing a large number of seconds
Your task is to write a function that prints it to the 
standard output (stdout) in the hours:minutes:seconds format

"""

def convert_seconds(seconds):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
  
    hours = seconds /60 /60
    minutes = seconds /60 %60
    seconds = seconds %60 %60
    
    print '%02d:%02d:%02d' % (hours, minutes, seconds)