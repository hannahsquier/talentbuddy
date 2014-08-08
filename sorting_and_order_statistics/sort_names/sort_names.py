"""
Take an array of first and last names, sort them into alphabetical order by last name, 
and then print them to the standard output (stdout) one per line.

"""

def sort_names(names):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"

   for name in sorted(names, key=lambda names: names.split()[1]):
       print name 
  
    

