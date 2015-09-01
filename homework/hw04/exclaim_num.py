"""
exclaim_num.py - 3 points
=====
Continually add exclamation points to a word as long as a user types in a
number from 1 through 3... 

* ask for a word
* then... repeatedly ask the user for a number from 1 - 3
* if the user types in 1 - 3, add that many *more* exclamation points (they
  accumulate from one iteration to the next) to the string
* after every answer, print out the new version of the word with exclamation
  points added
* if the user types in a number that's greater than 3 or less than 1, stop (DO
  NOT ADD any more exclamation points, and stop asking for a number)
* make sure to show the last version of the word with exclamation points at
  the end of the program
  
Example Output:

Run 1
-----
Please enter a word
> foo
How many exclamation points should I add (1 - 3)?
> 1
foo!
How many exclamation points should I add (1 - 3)?
> 3
foo!!!!
How many exclamation points should I add (1 - 3)?
> 98765
foo!!!!

Run 2
-----
Please enter a word
> foo
How many exclamation points should I add (1 - 3)?
> -2
foo
"""
