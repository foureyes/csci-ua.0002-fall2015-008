"""
together.py (4 points)
=====

Create a function called together:

* 2 parameters: takes a list of lists and a string as arguments
    * each inner list will have strings in it
    * the string argument will be used as a connector (see below)
* returns a new list
    * the returned list will be composed of strings formed from putting together the strings within the inner list
    * they will be put together using the connector string
    * you MUST use the join method on a string:
    * "x".join(["hi", "hey", "bye"]) --> hixheyxbye
* if there are less than 2 words in the inner list, do not include it in the outer list
* an empty list gives back an empty list
* examples:

together([['franken', 'word'],['key', 'tar']], '-') -> ['franken-word', 'key-tar']
together([['word'],['key', 'tar']], '*') -> ['key*tar']
together([], 'x') -> []
"""

