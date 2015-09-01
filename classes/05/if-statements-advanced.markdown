---
layout: slides
title: If Statements - Advanced 
---
<section markdown="block" class="title-slide">
# How to (Un)Complicate Things With If Statements
{% include title-slide-footer.html %}
</section>

<section markdown="block">
## elif
<aside>Like Smashing Together Your Two Favorite Keywords</aside>
</section>

<section markdown="block">
### elif Is the New _Else If_

We can use __elif__ to chain together a series of conditions.  This allows us to create multiple flows of execution (more than two), but - at most - only one path will be executed (even if more than one condition is true). 

* each condition is checked in order
* if the first is false, the next condition is checked
* this continues until the first true condition
* the body of code associated with that condition is executed
* the statement ends even if there are more conditions left
</section>

<section markdown="block">
### elif Syntax

* if statement like usual
* go back one level of indentation to mark that the previous code block has ended
* keyword __elif__
* condition
* colon
* body - indented, body ends when indentation goes back one level
* not required obv
* even if more than one true, only the first true executes!
* can add an else at the end
</section>

<section markdown="block">
### A Trivial elif Example

__Translate placement into Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal &rarr;__.  You can just us a hardcoded variable or ask for user input.

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/medals_elif.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Another elif Example
<aside>Let's have some more cake...</aside>
__Let's do the cake exercise (ask the user if they want cake) again with elif...__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_elif.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive If Statements?

__We could have impemented this using consecutive if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_consecutive_ifs.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive Nested If Statements?

__We could have impemented this using nested if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_nested_ifs.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### And How Did That Compare To Consecutive Nested If Statements?

__What do you think the decision trees look like?.__ &rarr; (Oh, and BTW, what's a decision tree? ...It's a graph that shows all possible decisions and the outcomes of those decisions.)

<div class="incremental" markdown="block">
![trees](../../resources/img/cake-decision-trees.png)
</div>
</section>

<section markdown="block">
### And How About Speed?

__We could make an educated guess.__ &rarr;

<div class="incremental" markdown="block">
* elif skips conditions if one of the early conditions is true!
* that means, best case, there are less instructions for the computer to execute when using elif
	* compared to nested ifs
	* or consecutive ifs
* not sure what the interpreter/compiler does behind the scenes when it translates, though
	* could optimize things 
	* produce similar machine code for both kinds of code
</div>
</section>

<section markdown="block">
### We're Not Finished Yet...
<aside>I'm bad at making decisions...</aside>

__What if we want to add "maybe" as a potential answer?  What about dealing with different ways of saying yes (like "yeah")?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_yeah_maybe.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Lastly, Everything Together

Ask the user for the results of two dice rolls.  The program should output the [name of the roll](http://en.wikipedia.org/wiki/Craps#Rolling) using Wikipedia's article on Craps.  Just do _Snake Eyes_, _Hard Fours_ and _Easy Fours_.

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/craps.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Nesting If Statements

* we saw this above to motivate our __elif__ example
* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block">
### Nesting If Statements Example

The coffee shop has a special for half price pastries on Fridays after 4 (16:00... or 16).  __Ask for day and time, and make a recommendation (buy now, wait x hours or don't buy).__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/pastry_buying_guide.py %}
{% endhighlight %}
</div>
</section>


<section markdown="block">
### How to Order Conditions

* if more than one condition in a series of elif's is true 
	* only the first true condition is executed!
	* other are skipped, including else
* be careful of conditions that never get evaluated 
	* an above condition may already account for it
	* here's an example...
</section>

<section markdown="block">
### How to Order Conditions Continued!

Here's a contrived exercise:  

* determine whether a number is 101 or if it's greater than 100
* if it's 101, it should only print out that it's "exactly 101" (it shouldn't print out greater than 100)

Here's an implementation.  __What gets printed if n = 200?  What gets printed if n = 101?__   &rarr;

{% highlight python %}
if n > 100:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</section>

<section markdown="block">
### How to Order Conditions Continued Some More!

__Of course, we could fix this.  There are a few ways...__ &rarr;

<div class="incremental" markdown="block">
* reordering
* using and
{% highlight python %}
if n == 101:
	print("exactly 101")
elif n > 100:
	print("more than 100")

if n > 100 and n != 101:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Equivalent Conditions
</section>

<section markdown="block">
### Logical Opposites 
A way to get rid of not operators is to use the opposite logical operator:

[Logical Opposites from THINKSCI](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)

* for example... the logical opposite of &gt; is &lt;=
* the logical opposite of &lt; is &gt;=

</section>

<section markdown="block">
### Logical Opposites Continued
__How can we rewrite this without the not?__&rarr;

{% highlight python %}
# Example from THINKSCI
if not (age >= 17):
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
if not (age < 17):
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
### De Morgan's Law
* not (x and y)  ==  (not x) or (not y)
* not (x or y)   ==  (not x) and (not y)
* THINKSCI example
	* uses combination of logical opposites and De Morgan's Law
	* clarity / closeness to original 

__Let's try truth tables for these!__ &rarr;
</section>

<section markdown="block">
### De Morgan's Law 
__How can we rewrite this?__&rarr;

{% highlight python %}
if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
if (sword_charge < 0.90) or (shield_energy < 100):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
## Truthiness and Style
</section>

<section markdown="block">
### Truthiness

See this [crazy chart](http://docs.python.org/py3k/library/stdtypes.html#truth-value-testing) on the _intrinsic_ boolean value of various types.  The following values are considered false:

* None
* False
* 0 of any numeric type (0.0, 0)
* empty mapping or sequence type (We'll look at these later) - this includes the empty string '', "", etc.
* some instances of user defined types based on __bool__ method
</section>
<section markdown="block">
### Truthiness Examples

{% highlight python %}
a = ""
if a:
	print("true!")

a = 0
if a:
	print("true!")

a = "foo"
if a:
	print("true!")
{% endhighlight %}

</section>

<section markdown="block">
### Another Note About Style
* remember idioms?
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values
* more elegant to test intrinsic truth values than using equality operator
{% highlight python %}
b = True
# instead of if b == True
if b:
	print("b")

s = "catz!"
# to test if the string exists
if s:
	print(s)

{% endhighlight %}

</section>

<section markdown="block">
### Let's Write a Mini Quiz Game!

__Write a program to ask a couple of questions about the book, Dune.__ &rarr;

{% highlight python %}
#  ______            _        _______ 
# (  __  \ |\     /|( (    /|(  ____ \
# | (  \  )| )   ( ||  \  ( || (    \/
# | |   ) || |   | ||   \ | || (__    
# | |   | || |   | || (\ \) ||  __)   
# | |   ) || |   | || | \   || (      
# | (__/  )| (___) || )  \  || (____/\
# (______/ (_______)|/    )_)(_______/
# 
# What is the name of the desert planet that's informally called Dune?
# > Arrakis
# You got it right!
# What valuable resource is only found on Dune?
# > cheese?
# Nope, the answer is: spice
# You got 1 questions right! 
{% endhighlight %}
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game (Continued)!

Let's get some requirements down:

* ask two questions sequentially
* keep track of the number of questions that the player got right
* output the number of questions right
* (optional) keep track of the number of questions wrong, and output that as well
* (optional) ask for the player's name and greet the player

</section>

<section markdown="block">
### We Don't Have To Jump Right Into Code!

__So, first, what's our plan?__ &rarr;

* flow chart?
* pseudocode?
</section>

<section markdown="block">
### Let's Write a Mini Quiz Game! (Continued Some More)!

What are some ways that we can be more tolerant about capitalization?  That is... what if we wanted to accept these answers:

1. Arrakis / arrakis
2. spice 4 / the spice / the spice melange

Another wrinkle might be to have different output based on which version of the _right_ answer was chosen.  For example, if someone puts in spice, it might say, "oh, you mean, _the spice melange_".
</section>


<section markdown="block">
## [Built-In Modules Are Up Next!](built-in-modules.html)
</section>
