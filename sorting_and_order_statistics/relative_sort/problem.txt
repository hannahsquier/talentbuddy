Given an array of integer numbers your task is to print to the standard output (stdout) 
the initial array, but sorted in a special way:

	-all negative numbers come first and their relative positions according to the initial 
	array do not change

	-the same with the positive integers, but they come last

Expected complexity: O(N) time, extra memory O(1)

Example input:
-5 2 1 -2 3

Example output:
-5 -2 2 1 3