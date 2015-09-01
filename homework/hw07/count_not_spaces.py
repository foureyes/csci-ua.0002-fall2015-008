"""
count_not_spaces.py (5 points)
=====

1.  Create a function called count_spaces:

    * takes one argument, a string
    * it returns the number of characters that are not spaces (' ') within
      that string

2.  Create at least two assertions to test your function.  Make sure to test
    for the following conditions:

    * if there are only spaces, the function should return 0
    * if there are characters other than space, the function should return the
      number of of those characters

3.  Lastly, call your function once at the end of your program:

    * call the function with the string, "A stitch in time saves nine"
    * assign the result of your function call to a variable
	* print out the variable

IPO
-----
input: a string
processing: go through every character in string, count the number of 
            characters that aren't spaces
output: the number of characters that aren't spaces


Example Usage
-----
s = "This or that"
result = count_not_spaces(s)
print(result)
# prints out 10
"""
