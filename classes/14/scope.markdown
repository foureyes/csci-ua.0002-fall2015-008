---
layout: slides
title: Scope 
---
<section markdown="block" class="title-slide">
# Scope
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Accessing a Variable Outside of a Function 

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope1.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Oddly... it's fine.  Something is printed out.  It seems like the function has access to s, which was declared outside of the function. 
</div>
</section>

<section markdown="block">
### How About Variables Declared Inside a Function?

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope2.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Uh-oh.  Looks like you can't access variables that are inside a function.
</div>
</section>

<section markdown="block">
### How About Parameters?

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope2b.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
This is the same as the previous slide.  You can't access the parameters (by their name) that you passed in to the function from outside of the function.
</div>
</section>

<section markdown="block">
### And Lastly... 

__What do you think will happen here?  Will something be printed out?  Nothing?  Or an error?__

{% highlight python %}
{% include classes/15/scope3.py %}
{% endhighlight %}

<div class="incremental" markdown="block">
Hmmm... it looks like names created within a function are _local_ to that function.  They don't override names in the global space.
</div>
</section>

<section markdown="block">
### What Does This All Mean?

A __scope__ holds the current set of available names (variables) and the values that they point to.  

* anything that we define in the top level of indentation our program is said to be in the __global scope__
* in the following example, the variables _a_ and _b_ are in the __global scope__
* they can be accessed from anywhere, even within the function

{% highlight python %}
a, b = 25, "something"

def foo():
	c = "bar"
	print(b)
	print(c)
# what will this print out?
foo()
{% endhighlight %}
</section>

<section markdown="block">
### Scope

Variables that are defined in your function (one indentation level in), however, are only available within your function.  They are _local_ to that function.  The example below won't work.

{% highlight python %}

def foo():
	c = "bar"
	return c

print(c)
{% endhighlight %}
</section>

<section markdown="block">
### Scope Continued

Furthermore, variables that are declared within a function that have the same name as a global variable are totally different variables/values!  They don't overwrite the outer, global variable (there's a way to do this, though).  What will this print?

{% highlight python %}
c = "on toast"
def foo():
	c = "grape jelly"
	print(c)

foo()
print(c)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
grape jelly
on toast
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Scope Summary

* variables declared outside of a function can be accessed within a function
* variables declared inside of a function cannot be accessed outside of a function (they're __out of scope__)
* parameters in a function cannot be accessed outside of a function either
* variables declared within a function don't override those declared outside of a function
</section>


<section markdown="block">
### A Quick Look At Turtle

There's a small difference between these two functions.  __What is it?  Do both functions _work_?__

Program 1:

{% highlight python %}
# other setup code implied
t = turtle.Turtle()
def draw_blue_line(length):
	t.color('blue')
	t.forward(length)
{% endhighlight %}

Program 2:

{% highlight python %}
# other setup code implied
t = turtle.Turtle()
def draw_blue_line(t, length):
	t.color('blue')
	t.forward(length)
{% endhighlight %}
</section>

<section markdown="block">
### Turtle Continued

* both functions work fine
* the first snippet of code relies on a turtle named t to exist outside of a function definition
* what if we had two turtles that we wanted to use the function on?  
* we'd have to pass the turtle in, otherwise the function would only be good for one turtle
</section>

<section markdown="block">
### Two Turtles 

__(btw, what would happen if I didn't pass in t?  let's try it...)&rarr;__
{% highlight python %}
import turtle
def draw_blue_line(t, length):
	t.color('blue')
	t.forward(length)
wn = turtle.Screen()
don = turtle.Turtle()
leo = turtle.Turtle()

don.up()
don.goto(100, 100)
don.down()

draw_blue_line(don, 200)
draw_blue_line(leo, 100)
wn.mainloop()
{% endhighlight %}
</section>
