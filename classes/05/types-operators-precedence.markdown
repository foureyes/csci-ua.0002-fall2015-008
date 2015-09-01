---
layout: slides
title: Types and Operator Precedence 
---

<section markdown="block" class="title-slide">
# Types, Operators, and Precedence
{% include title-slide-footer.html %}
</section>


<section markdown="block">
### Types

__We know about four or five types.  What are they?__

<div class="incremental" markdown="block"> 
* str
* int
* float
* bool
* (complex)
</div>
<div class="incremental" markdown="block"> 
</div>
</section>

<section markdown="block">
### Functions

__What's a function?  We know about seven built-in functions.  What are they?  What values do they expect?  What do they return?__

<div class="incremental" markdown="block"> 
* print - doesn't return anything
* type
* int
* str
* float
* bool
* input - always returns a string!
</div>
</section>

<section markdown="block">
### Types and Operations

__What are some numeric operations that we've used?__

<div class="incremental" markdown="block"> 
* __+__
* __-__
* __/__
* __//__
* __\*\*__
* __%__

(you can mix and match numeric types, __but not other types__)
</div>
</section>

<section markdown="block">
### Types and Operations (Continued)

__What are some string operations that we've used?__

<div class="incremental" markdown="block"> 
* __+__ - concatenation - only strings
* __\*__ - multiplication - string and int!
* __%__ - interpolation - only strings \* sort of
</div>
</section>

<section markdown="block">
### Let's Talk About Comparison Operators

__What are the six comparison operators that we learned about, and how do they work with different types?__

<div class="incremental" markdown="block"> 
* __==__ - different types always return False
* __!=__ - different types always return True
* __<__ - different non numeric types result in an error
* __>__ - different non numeric types result in an error
* __>=__ - different non numeric types result in an error
* __<=__ - different non numeric types result in an error

</div>
</section>

<section markdown="block">
### Let's Talk About Logical Operators

__What are the three logical operators that we learned about?__

<div class="incremental" markdown="block"> 
* and
* or
* not
</div>
</section>

<section markdown="block">
### What Order Do All of These Operators Go In?

__So.  With all of these operations, which ones take precedence?__

<div class="incremental" markdown="block"> 
1. Parentheses
2. Numerical/String operators
3. Comparison operators
4. Logical operators
	1. not
	2. and
	3. or
</div>
</section>

<section markdown="block">

### Conditionals

* syntax - if, condition, colon, indented body
* note that the end result of comparisons... are essentially the same as bare literal
* some example code I have takes the shortcut of putting in the bool literal
{% highlight python %}
a, b = 1, 1
if a == b or b == 1 or a == 1:
	print("true")

if True:
	print("true")
{% endhighlight %}
</section>

<section markdown="block">
### Review Answers to Handout
[Sooo... with all of that said, let's go over the answers to the handout from the previous class!](../../resources/handouts/class05/input-types-if.pdf).
</section>

<section markdown="block">
## [How to Complicate Things With If Statements](if-statements-advanced.html)
</section>
