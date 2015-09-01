"""
unique.py - 5 points
=====

1. Create a function called get_unique_values
2. The function should take one argument, a list named values
3. The function should return a new list composed of only the unique values 
   in the original list of values
4. An empty list should result in an empty list
5. Ignore the case where the function receives a value that is not a list
6. Write four assertions for the example output below

Hints:

* it may help to start with a new empty list and build from there
* how do you determine if something is a duplicate / already exists?  There
  may be operators, methods or functions that may help you

Example Output:
-----

>>> print(get_unique_values(['foo', 'foo', 'bar', 'baz', 'bar']))
['foo', 'bar', 'baz']
>>> print(get_unique_values([1, 1, 1, 1, 1]))
[1]
>>> print(get_unique_values([]))
[]
>>> print(get_unique_values(["just me"]))
['just me']
"""
