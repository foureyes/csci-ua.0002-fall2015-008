"""
sort_words.py (6 points)
=====
Create a function called sort_words, that splits up a single string into two
lists nested in one larger list. One list will have words that have a length
less than or equal to a specified partion number, and the other list will
have words that are longer than that partition.

For example: "An awkard aardvark ate an apple!", with a partition of 3, would
give back [["an", "ate", 'an"],["awkard", "aardvark", "apple"]]

* it should have two parameters, a sentence and a partition length
* it will assume that the words in the sentence are separated by a space
* it will extract individual words from a sentence by:
  * collecting every character in the sentence into a word
  * ignoring punctuation marks
  * until the character is a space
  * at which point, the word is placed in the appropriate list
    * if the word is smaller than the partition, place it in the first list
    * if the word is larger than the partiion, place in in the second list
  * then start collecting the next word
  * hint: don't forget to collect the last word!
  * both lists should be placed in another list (small words first, large
    words second.
  * the function should return the resulting list of lists
* call your function on the following sentence:
  * "Holly hesitated, having hurled her hamburgers high."
  * use a partiion of 5
  * save the result into a variable
  * print out the last element of the last list

    
"""


