"""
upper_and_constrain.py (7 points)
=====
Create two functions, upper and constrain. Both require the use of indexes
during iteration in order to change the argument passed in (rather than
returning a value)

upper
-----
1. Create a function called upper
2. It should have one parameter, words, a list of strings (you do not have to
   handle invalid arguments)
3. It should not return anything (no return statement)
4. It will make very word in the list, words, uppercase
5. After defining the function:
   a. Create a list, my_words, that contains the strings:
      "cactii", "captivate", "curious", and "cats"
   b. Print out the string, "my_words before", and then the list, my_words
   c. Call your upper function, pass in my_words as the argument
   d. Print out the string, "my_words after", and then the list, my_words again

constrain
-----
1. Create a function called constrain
2. It should have three parameters (you do not have to handle invalid
   arguments)
   a. numbers, a list of numbers
   b. min_value, a number that represents the minimum value that is allowed
      in the list
   c. max_value, a number that represensts the maximum value that is allowed
      in the list
3. It should not return anything (no return statement)
4. It will go through the entire list of numbers...
   a. if a value is above the max value or below the min value, it should be
      changed to the min value or max value respectively
   b. if the value is within the min and max, it should remain the same
5. After defining the function:
   a. Create a list, my_numbers, that contains the numbers:
      5, 1, 7, 4, -1, 2, 1, 8, 3, 6
   b. Print out the string, "my_numbers before", and then the list, my_numbers
   c. Call your constrain function, pass in my_numbers as the list to be
      changed, and use 1 and 7 as your min and max values
   d. Print out the string, "my_numbers after", and then the list, my_numbers
      again

Example Output
-----
my_words before: ['cactii', 'captivate', 'curious', 'cats']
my_words after: ['CACTII', 'CAPTIVATE', 'CURIOUS', 'CATS']
my_numbers before: [5, 1, 7, 4, -1, 2, 1, 8, 3, 6]
my_numbers after: [5, 1, 7, 4, 1, 2, 1, 7, 3, 6]
"""

