---
layout: slides
title: String Objects, String Methods, Built-Ins
---
<section markdown="block" class="title-slide">
# String Objects, String Methods, Built-Ins
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Objects and Methods (Again!)

__What's an object?  What's a method?  Give some examples. &rarr;__

<div class="incremental" markdown="block">
* __object__ - a _thing_ that a variable name can refer to, like a screen, turtle, string or integer
* for us that means attributes (data) and methods (functions)... all packed into one thing
* a __method__ is essentially a function that's associated with a particular object
* a __methods__ can be thought of as an action behavior that an object can perform
</div>
</section>

<section markdown="block">
### Calling Methods

How do you call a method?  For example, if you had a turtle object that's named leo, __how would you call the forward method on it to tell it to move forward 100 pixels? &rarr;__

{% highlight python %}
leo = Turtle()
# tell leo to move forward
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
leo = Turtle()
leo.forward(100)
# use the object name
# followed by dot
# and the method (from here, it's like a regular function)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Strings as Objects!

Yes __strings__ are objects too (just like turtle)  Here are some methods.  __Let's try them out! &rarr;__

1. __upper__() 
2. __lower__()
3. __isdigit__()
4. __isalpha__()
5. __find__(sub[, start[, end]])
6. __format__(...)
7. __strip__([chars])

</section>

<section markdown="block">
### upper() and lower()

__upper__() and __lower__() return the string that the method was called on in either all uppercase or all lowercase.  __What would the following print out? &rarr;__

{% highlight python %}
print("this should be uppercase".upper())
print("THIS SHOULD BE LOWERCASE".lower())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
THIS SHOULD BE UPPERCASE
this should be lowercase
{% endhighlight %}
</div>
</section>

<section markdown="block">
### isdigit() and isalpha()

__isdigit__() and __isalpha__() test whether a string is only numbers or letters (both return False if empty string).  __What would the following print out? &rarr;__

{% highlight python %}
print("123".isdigit())
print("1.23".isdigit())
print("one two three".isdigit())
print("onetwothree".isalpha())
print("one two three".isalpha())
print("one!".isalpha())
print("1".isalpha())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
True
False
False
True
False
False
False
{% endhighlight %}
</div>
</section>



<section markdown="block">
### find()

__find__() returns the first index where the argument (a character or substring) is found.  It returns -1 if the substring is not in the original string.

{% highlight python %}
print("hello".find("h"))
print("hello".find("x"))
print("hello".find("lo"))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
0
-1
3
{% endhighlight %}
</div>
</section>

<section markdown="block">
### strip()

__strip__() removes leading and trailing whitespace (it can also remove other leading and trailing characters).  What do you think this results 

{% highlight python %}
print("  spaces all around   ".strip())
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
spaces all around
{% endhighlight %}
</div>
</section>

<section markdown="block">
### format()

Format is like the string interpolation operator, but possibly easier?! 

* instead of %s, use curly braces and the number of the argument as a placeholder {0}, {1}
* numer corrseponds to each argument in the call, 0 being the first
* __What do you think the following returns? &rarr;__

{% highlight python %}
"{0} elephants".format("twenty")
"{0} elephants".format(20)
"{0} elephants".format(20, 100)
"{1} elephants".format(20, 100)
"{0} elephants and {1} peanuts".format(20, 100)
{% endhighlight %}
</section>

<section markdown="block">
### format() results

{% highlight python %}
twenty elephants
20 elephants
20 elephants
100 elephants
20 elephants and 100 peanuts
{% endhighlight %}
</section>

<section markdown="block">
### The Built-In len() Function

__len__ is a built-in function that Returns the length of a sequence

* it is __not a method__, so you do not call it on an object
* however, you can pass a value to it, and it will return its length
* for strings, it will return the number of characters
* last index is the len(s) - 1

{% highlight python %}
print(len("cat"))
# gives 3
{% endhighlight %}
</section>

<section markdown="block">
### A Couple of Exercises:

* use upper or lower to check for permutations for input
	* for example, loop forever
	* ask the user if they want the loop to stop
	* accept "Yes", "YES", "yes", etc.
* rewrite get_first_word, but use __find__() instead of a loop
</section>

<section markdown="block">
## [Lists](lists_intro.html)
</section>
