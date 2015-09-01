"""
tip.py (6 points)
=====
Create a tip calculator. You will have to do additional research (online or in
the required book, Starting Out with Python) for the last part, number 6, in 
this program.

1. Print out a nice welcome banner!
2. The program should ask the following:
   a. How many people?	
   b. How much did it cost?
   c. If there are less 6 people, ask: How was the service?  
   d. The values that the service can be are: terrible, poor, ok, good, great
3. If the number of people are greater than or equal to 6, the tip should 
   always be 20%, regardless of service (service should not be asked for if 
   there are greater than 6 people anyway) 
4. Otherwise (less than six people), calculate the tip using the following 
   table:
   * terrible = no tip (0%)
   * poor - 10%
   * ok - 15%
   * good - 20%
   * great - 25%
   * any other input - default to 20% and output a message saying that the
     default tip value will be used
5. Output the calculated tip.
6. Find out how to format the number so that there are only 2 decimal places.
   (Do research on the format function by looking online or reading pages 68
   and 69 in the book, Starting Out With Python, 3rd Edition)

Example Output (consider text after the ">" user input):

Run 1: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 2
How much did it cost? > 25
How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
Run 2: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 4
How much did it cost? > 70
How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 20 percent.
You should probably tip $14.00!

Run 3: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 200
How much did it cost? > 950
You should probably tip $190.00!
"""
