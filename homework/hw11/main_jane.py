"""
main_jane.py - (Extra Credit - up to 3% on lower midterm grade if your first
               midterm score was not dropped.) 
====
Write a program that will count the frequency of words that start with an 
uppercase letter in Pride and Prejudice.  Print out words that occur more than 
200 times.  Look at the result and determine which character was mentioned the 
most!

1. Download a copy of Pride and Prejudice by Jane Austen from Project 
   Gutenberg:
   http://foureyes.github.io/csci-ua.0002-spring2015-008/homework/hw11/pg1342.txt
2. Save it into the same directory that your Python program is in.  
3. Read in the contents of the file. 
4. Isolate every word in the file; assume words are separated by spaces .
5. Clean each word by removing punctuation and trailing and leading spaces (this
   includes new lines).
6. If the first letter of the word is uppercase, keep track of its count!
7. Use a dictionary to store the count of each word - the key should be the 
   word and the value should be the number of times that word appears in the
   text.
8. Print out all of the words that occur more than 200 times.
9. The output should be similar to:

Jane 263
Mr 783
Mrs 343
She 325
Elizabeth 594
The 285
.
.
.

Aside from using a dictionary, feel free to implement this program in any way
you wish (creating function(s) to organize your program, using any of the 
constructs or objects and methods that we've used throughout the class, etc.).

Hints:
* dictionary methods such as .get() or .items() may be useful
  * http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/25/dictionaries.html
* string methods may be helpful for cleaning and isolating words
"""
