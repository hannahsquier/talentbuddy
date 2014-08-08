"""Given a string of open and closed brackets output "Balanced" 
if the brackets are balanced or "Unbalanced" otherwise.
A string is balanced if it consists entirely of pairs of 
opening/closing brackets (in that order), none of which mis-nest."""

def balanced_brackets(s):
    # Write your code here
   
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i ==')':
            count -= 1
        if count < 0:
            print 'Unbalanced'
            return
    if count == 0:
        print 'Balanced'
    else:
        print 'Unbalanced'
