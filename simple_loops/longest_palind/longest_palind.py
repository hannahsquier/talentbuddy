"""
Given a string S, find the longest substring in S 
that is the same in reverse and print it to the standard output.

"""

def longest_palind(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    pals = {}
    pal_start = 0
    
    
    while pal_start < len(s):
        pal_end = 1
        while pal_end <=len(s):
            pal = s[pal_start:pal_end]
            if pal == pal[::-1]:
                pals[pal] = len(pal)
            
            pal_end += 1
           
        pal_start +=1
        
            
            
   
    print pals.keys()[pals.values().index(max(pals.values()))]