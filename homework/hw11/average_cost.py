"""
average_cost.py (10 points)
=====
Create a program that reads in a file of meal costs per day of week, and allows
the user to get information about the average cost per day.

1. Read in a file of meal costs per day of week
    * http://foureyes.github.io/csci-ua.0002-spring2015-008/homework/hw11/daily_meal_spending.txt
    * the 1st column is the day-of-week
    * the remaining columns are the costs for the meal for that day
2. Calculate the average cost per meal per day and store the results in a
   dictionary
    * loop over every line in the file
    * extract data from each line (hint: how do you create a list from a
      string)
      * get the name of the day
      * get the costs (hint: slicing may work here)
      * loop over the costs to calculate the average (hint: this will be a
        nested loop)
    * use the day's name as the key, and store the average for that day as a
      value in a dictionary ... for example "Tuesday": $8.63
3. Ask the user for a command: get average for specific day, all days or quit
    * continually ask the user for a command:
      * Enter (day), (a)ll or (q)uit
    * if the user enters 'q', stop asking, and end the program
    * if the user enters 'a', print out all of the days and average costs in
      the dictionary (order does not matter)
      * (hint: loop over the dictionary you created from part 2)
      * (hint: a dictionary's .items() method may be helpful, but you don't
        have to use it)
    * if the user enters anything else:
      * if it's a key that's in the dictionary (that is, if it's a valid day
        name, such as Monday, Tuesday, etc.) print out the average cost for
        that day only
        * (hint: try/catch with a KeyError is one way to do this)
        * (hint: another way is to check if the key exists first)
        * (hint: ...and lastly, you can use the dictionary's .get() method)
      * otherwise, print out "That's not a valid day"

Example output:
=====
Enter (day), (a)ll or (q)uit
>a
Average for Monday: $7.50
Average for Tuesday: $8.63
Average for Friday: $13.60
Average for Saturday: $4.25
Average for Wednesday: $7.67
Average for Sunday: $9.29
Average for Thursday: $12.92
Enter (day), (a)ll or (q)uit
>Sunday
Average for Sunday: $9.29
Enter (day), (a)ll or (q)uit
>Tuesday
Average for Tuesday: $8.63
Enter (day), (a)ll or (q)uit
>Caaaaaturday
Please enter a valid day
Enter (day), (a)ll or (q)uit
>q
"""

    
