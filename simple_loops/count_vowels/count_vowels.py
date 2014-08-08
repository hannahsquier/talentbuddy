"""Given a string write a function that 
prints to the standard output (stdout) the 
number of vowels it contains"""

def count_vowels(s):
    vowel = 'aeiouAEIOU'
    count = 0
    for letter in s:
        if letter in vowel:
            count+=1
    print count
