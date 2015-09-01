"""
guess.py - 7 points
=====

This one has a lot of parts, but it should be pretty fun!

Create a number guessing game.  The game will create a secret number.  It will
keep asking the user for a guess, and it will keep asking if they give up.  It
will continue asking these questions until either the user gives up or guesses
correctly.  Here are the detailed steps:
 
1.  generate a secret number between 1 and 10 (inclusive)
2.  tell the user that "I'm thinking of a number from 1 through 10"
3.  ask the user to guess the number
4.  keep track of the number of guesses
5.  if the guess is incorrect, print the following messages:
    * if the guess is within 1 of the secret number, say "That's really close!"
    * if the guess is not within 1, say "Sorry - that's not it"
    * in either case of an incorrect guess (within 1 or not), ask the user if
      they give up
    * if the user does not say "yes" or "Yes" to giving up, ask for a guess
      again (go back to step 1)
    * if the user says yes to giving up stop asking questions and reveal the
      secret number: "The secret was [secret number]"
6.  if the guess is correct, print the following message:
    * You got it! You only had to guess [number of guesses] times!

Hints:
-----
* use the random module (see the slides from class 7) for you secret number
* use the abs function (see the slides from class 7) for determining within 1
* a nested if statement may be helpful (though perhaps not necessary)

Example Output 1: Guessing wrong
-----
I'm thinking of a number from 1 through 10.

Guess what number I'm thinking of.
> 3
You got it! You only had to guess 1 times!


Example Output 2: Guessing wrong, not giving up
-----
I'm thinking of a number from 1 through 10.

Guess what number I'm thinking of.
> 5
Sorry - that's not it!
Give up?
> no
Guess what number I'm thinking of.
> 2
You got it! You only had to guess 2 times!


Example Output 3: Close guess, not giving up, guess wrong, giving up
-----
I'm thinking of a number from 1 through 10.

Guess what number I'm thinking of.
> 4
That's really close!
Give up?
> no
Guess what number I'm thinking of.
> 3
Sorry - that's not it!
Give up?
> yes
The secret was 5
"""
