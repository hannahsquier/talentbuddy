def fizzbuzz(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    lst = range(1, n+1)
    for num in lst:
        if num % 3 == 0 and num % 5 == 0:
            num = 'FizzBuzz'
        elif num % 3 == 0:
            num = 'Fizz'
        elif num % 5 == 0:
            num = 'Buzz'
        print num

