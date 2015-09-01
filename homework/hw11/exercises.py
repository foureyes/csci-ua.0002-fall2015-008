"""
excercises.py - 9 Points
====
Follow the instructions in the comments below.  

* Write code below each comment.
* There are 9 steps total.
* Run your code to view the output.
* Make sure there are no syntax errors (this file should be runnable).
"""

# 01. Create a list called pairs that consists of 3 tuples, with each tuple 
#     having 2 elements.  The first tuple should contain the elements 1 and 2, 
#     the second tuple should contain 11 and 12, and the last tuple should 
#     contain 21 and 22.  
#
#     Print out your list (pairs).
"""
Example Output
-----
[(1,2), (11,12), (21,22)]
"""


# 02. Iterate over the list using a for loop, but use tuple unpacking / multiple 
#     assignment to set two loop variables.  Use these two loop variables to 
#     print out both elements in every tuple, separated by a + sign, and print 
#     out and equals sign and the sum of both elements.  The output should look 
#     similar to this:
#     1 + 2 = 3
#     11 + 12 = 23
#     21 + 22 = 43
"""
Example Output
-----
1 + 2 = 3
11 + 12 = 23
21 + 22 = 43
"""


# 03. Create a variable called t and set it equal to the value that results from 
#     popping the last element off of your list of tuples.  
#
#     Print out both the value and type of t:
#     <class 'tuple'>
#     (21, 22)
"""
Example Output
-----
<class 'tuple'>
(21, 22)
"""


# 04. Tuples are immutable.  Try changing the element at index 0 of your tuple, 
#     t, so that it is equal to 100.  What happens?  Prevent an error from 
#     ocurring by wrapping your assignment statement in a try except.  Except the
#     specific type of error that is caused when trying to use assignment on a
#     tuple (you can determine this by observing the error that occurs when
#     running your program).  
#
#     In you except block, print out "Tuples are immutable".
"""
Example Output
-----
Tuples are immutable
"""

   
# 05. Create a dictionary called person - it should have 3 name value pairs:
#     key is "first name", value is "Mabel"
#     key is "last name", value is "Pines"
#     key is "workplace", value is "Mystery Shack"
#
#     Print out your dictionary (person) and print out the value at key 
#     "workplace" using indexing.  The output should look something like:
#     { ... intentionally blank ... }
#     Mystery Shack
"""
Example Output
-----
{(should show your dictionary)}
Mystery Shack
"""


# 06. Try indexing into your dictionary with a key that doesn't exist - print
#     print out the element at key 'pet' (again, a key that doesn't exist).  
#     This should cause an error!  Note the error that occurs and use try/except
#     to prevent the specific error that is happening.
# 
#     In you except block, print out "That key doesn't exist yet!"
"""
Example Output
-----
That key doesn't exist yet!
"""

   
# 07. Add another key/value pair to the dictionary by indexing into your
#     dictionary with a key that doesn't exist yet... and assigning a value to 
#     it.  The key/value pair to add is "pet" and "Waddles" respectively.  Note
#     that this does *not* cause an error!
#
#     Print out the entire dictionary again.  It should show the new pair.
"""
Example Output
-----
{(should show your dictionary with pet key added}
"""


# 08. Use a for loop to iterate through your dictionary.  In the body of your
#     for loop, print out your loop variable.  You should see that only the keys
#     are printed out (note that the order may be different):
#     last name
#     first name
#     pet
#     workplace
"""
Example Output
-----
workplace
first name
last name
pet
"""


# 09. Iterate through calling the items method on person: person.items()...
#     and use tuple unpacking/multiple assignment within the for loop itself to
#     create two loop variables.  The first loop variable should be key, the
#     second should be value. In your loop body, print out both key and value:
#     last name Pines
#     first name Mabel
#     pet Waddles
#     workplace Mystery Shack
"""
Example Output
-----
workplace Mystery Shack
first name Mabel
last name Pines
pet Waddles
"""










