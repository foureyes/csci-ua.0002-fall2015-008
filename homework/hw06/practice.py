"""
practice.py (6 points)
=====
This exercise is about None, returning values from functions, and global
variables. You'll define three functions below, call them, and print out 
the results. You'll also have to print out a message explaining each. The
instructions for each function are in the comments below. Make sure to read
them carefully! Lastly, keep the existing print statements intact.

When finished, the program should run without any errors, and should have
a few lines of output based on the instructions.
"""

print('=====\n#1')
# 1. a. Create a function called nothing_for_you. 
#    b. It should have one parameter called message.
#    c. Within the body of your function print out the sentence "Inside 
#       function nothing_for_you ", along with the message passed in. 
#    d. After your function definition, (that is, after both the header and
#       the body, completely outside of the function), set a variable called 
#       result equal to the result of calling the function that you just 
#       created. Pass in one argument to your function call: "just printing". 
#    e. Print out the result variable.
#    f. Print out a sentence explaining what value is in result and why:
#       print('result is ... because ...')


print('=====\n#2')
# 2. a. Create a function called format_money.
#    b. It should have one parameter called value.
#    c. It will give back the value prefixed with a dollar sign and with two
#       two decimal places: $74.00 (as an example).
#    d. Remember, to give back a value, you will need to use the return 
#       statement.
#    e. To ensure that the new value has two decimal places, use format with
#       the format string, '.2f' (also note that format gives back a string).
#    f. Remember to prefix your newly formatted value with a dollar sign.
#    g. After your function definition, set a variable called money equal to
#       the result of calling the function that you just created. Pass in one
#       argument to your function call: 7.
#    h. Print out the money variable.
#    i. Print out a sentence explaining what value is in the money variable and
#       why: print('money is ... because ...')


print('=====\n#3')
# 3. a. Create a global variable called thing_to_add, and set it equal to 5.
#    b. Create a function called add_global.
#    c. It should have one parameter called x.
#    d. It will give back the value of x added to the global variable,
#       thing_to_add.
#    e. After your function definition, set a variable called num equal to the
#       result of calling the function that you just created. Pass in one
#       argument to your function call: 20.
#    f. Print out the num variable.
#    g. Print out a sentence explaining what value is in the num variable and
#       why an error did not occur!
#    h. Additionally, print out a sentence explaining what would happen if you
#       tried to access the variable x after the function definition. 
