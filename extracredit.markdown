---
layout: default
title: Extra Credit
---

<style>
h1 { 
	text-decoration: underline;
}
.highlight {
	padding: 0.5em 1em 0.5em 1em;
	background: #000;
	color: #fff;
	width: 50%;
}
code {
	background: #000;
	color: #fff;
}
</style>

rps.py 
=====

Extra Credit Assignment
-----

* __Due May 8th, before 11pm__
* __10 points total__
* __These points will count as percentage points on your lower midterm exam grade__
* __Create a text-based [rock-paper-scissors](http://en.wikipedia.org/wiki/Rock-paper-scissors#Game_play) game.__


Instructions
-----

1. download the assignment: [rps.py](extracredit/rps.py)
2. continually ask the user for a command (until the user types in q to quit)
	* the command can be r, p, s, h, or q
	* r, p, s correspond to rock, paper and scissors
	* h corresponds to history
	* q corresponds to quit
3. if the command is __r, p, or s__:
	* create a move for the computer
	* the computer's move should be generated by a function that you write
		* __this function should be placed in a module in a file separate from
		  your actual program__ file; name the module __rpshelper.py__ (see the
		  [slides on creating your own modules](http://localhost:8000/classes/23/modules.html))
		* implement a function called get_computer_move that takes two 
		  parameters: a list called their_moves and a list called your_moves.
		* the variable, their_moves, represents the other player's moves, and 
		  the variable your_moves represents the computer's moves. 
		* use the history of the player's moves and/or the computer's moves to
		  determine what the next computer move should be.  Use any algorithm
		  you want (even random choice!):
			* for example, you can use the last element of their_moves to 
			  make decisions on what the computer should do next... or count 
			  frequencies in their history to predict the opponent's next move
			* in a comment, write out what your algorithm is supposed to do
			* however, make sure *not to mutate* the original list!  Either 
			  clone your list (a = their_moves[:]) or don't use methods that 
			  mutate the original list.
			* it should return the letter 'r', 'p', or 's' depending on what 
			  result your algorithm generates.
		* use this module and function in your main rps.py program
	* if it's a win, add a point to winner's (either player or computer) score
	* if it's a tie, don't add any points
	* print out both the player's move and the computer's move
	* print out who won
	* print out current point totals
4. if the command is __h__:
	* show a list of all of the computer's previous moves
	* show a list of all of the player's previous
5. if the command is __q__:
	* quit the game
6. ask for input again... (continually until the input is q)
7. you can add additional features to the game for more points (see below)


Example Output ('base' version of game):
-----

(Characters after > is user input)

{% highlight python %}

(r)ock, (p)aper, (s)cissors, (h)istory or (q)uit
>r
PLAY: player: r, computer: p
computer wins
SCORE: player: 0, computer: 1
==========================================

(r)ock, (p)aper, (s)cissors, (h)istory or (q)uit
>s
PLAY: player: s, computer: p
player wins
SCORE: player: 1, computer: 1
==========================================

(r)ock, (p)aper, (s)cissors, (h)istory or (q)uit
>h
Player     Computer
------     --------
r          p
s          p
==========================================

(r)ock, (p)aper, (s)cissors, (h)istory or (q)uit
>r
PLAY: player: r, computer: r
tie
SCORE: player: 1, computer: 1
==========================================

(r)ock, (p)aper, (s)cissors, (h)istory or (q)uit
>q
{% endhighlight %}


Point Details
-----

* __2 points__  - submitting an attempt
* __2 points__ - no syntax errors in submission and reasonable effort shown
* __1 point__  - game is playable (basic interaction; input and output)
* __1 point__  - implement a function to determine what the computer's move will be
* __1 point__  - implement the above function in an external module
* __2 points__  - correctly implementing a majority of the game logic and rules
* __1 point__  - correctly implementing all game logic and rules
