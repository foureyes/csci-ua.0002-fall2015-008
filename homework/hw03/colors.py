"""
colors.py (5 points)
=====
Starting Out with Python, Chapter 4, Programming Exercises #5 (page 153)

5. The colors red, blue, and yellow are known as the primary colors because
   they cannot be made by mixing other colors.  When you mix two primary 
   colors, you get a secondary color, as shown here:

     When you mix red and blue, you get purple.
     When you mix red and yellow, you get orange.
     When you mix blue and yellow, you get green.
  
   Design a program that prompts the user to enter the names of two primary 
   colors to mix.  If the user enters anything other than "red", "blue", or 
   "yellow", the program should display an error message.  Otherwise, the 
   program should display the name of the color that results.

Note: the book does not account for specific requirements in its instructions:

* you can display the error message after both colors were entered
* if both colors entered are primary colors, but they are the same, you can 
  just output the same color


Example Output - Everything after the greater than sign (>) is user input:

Example 1
------
Please enter primary color 1 (red, blue and yellow)
> blue
Please enter primary color 2 (red, blue and yellow)
> yellow
The primary colors, blue and yellow, combine to make the secondary color, green.

Example 2
------
Please enter primary color 1 (red, blue and yellow)
> blue
Please enter primary color 2 (red, blue and yellow)
> blue
The primary colors, blue and blue, combine to make the secondary color, blue.

Example 3
------
Please enter primary color 1 (red, blue and yellow)
> blue
Please enter primary color 2 (red, blue and yellow)
> gold
At least one of the colors you entered is not a primary color.
"""
