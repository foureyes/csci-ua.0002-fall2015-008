"""
pig_latin.py (6 points)
=====

Write a function that translates a word into pig latin

http://en.wikipedia.org/wiki/Pig_Latin

Our version of Pig Latin will follow these rules
-----
* everything automatically gets converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels?  this sample program does something similar:
  http://foureyes.github.io/csci-ua.0002-spring2015-008/classes/17/review.html#28.0 
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

The function should have the following input and output:
-----
* takes a string as an input  
* returns a string (the pig latin translation of the string)
"""
