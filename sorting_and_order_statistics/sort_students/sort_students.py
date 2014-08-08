"""
implement the bubblesort algorithm to sort the array in ascending order and 
print the sorted elements to standard output (stdout), one per line

"""

def sort_students(numbers):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    changed = True
    while changed:
        changed = False  
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                changed = True
    for number in numbers:
        print number