"""
starry_starry_night.py (15 points)
=====
Draw some stars! 

Requirements
-----

### Part 1

* customize the colors of your drawing (choose whatever colors you like)
    * change the background color
    * set the pen color
* turn animation off (we're going to be drawing a lot of stars)
* set the width and height to 800 width and 600 height
* create a function called __draw star__
    * you can draw whatever star you like
    * the examples show a typical 5 pointed star
    * parameters: x, y and size
    * processing: it will draw a star at the x and y location specified, and the size of the star; you can take that to mean the size of a side (easier), or the entire star 
    * return: does not return anything
    * don't forget to call update at the end of it
* call your function once to draw a star in the middle of the screen

![star middle](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_1.png)

### Part 2

* comment out your function call for drawing a single star from the previous part
* now, instead of drawing a single star, draw several stars using a for loop
* they can be drawn in a straight line horizontally or vertically
* or... if you want to get fancy, draw them in a curve
* see the examples below:

![stars in a row](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_2.png)

![stars curved](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_3.png)

### Part 3

* again, comment out your code for drawing several stars from the previous part
* now, create another function called __generate_star_data__
    * this function will generate a list of lists that represents star data:
        * the first element in the sub list will represent an x value, the second represents a y value, and the last represents size
        * for example, [[0, 0, 10], [200, 200, 80]] represents 2 stars, one at the origin... and a larger star on the upper right hand corner
    * parameters: an int that represents the number of elements in the list (the number stars / sub lists)
    * processing: 
        * it will randomly generate x, y, and size values, put these values into a list... 
        * and add this three element list to the star list (the list of lists)
        * the bounds of the random numbers that you generate can be hard coded based on the width and height of the window
    * return: the list of lists representing stars
* example usage below:

<pre>
star_data = generate_star_data(2)
print(star_data)
# prints out: [[-250, 121, 49], [100, 0, 20]] 
</pre>

### Part 4

* use the function from the previous part to generate a list of 40 stars (a list of 40 sub lists)
* save the result of this into a global variable (that is, it should be a variable defined outside of all of your functions)
* create a function called draw_sky:
    * within it, iterate through the global list you created 
    * draw a star based on the data in the sub list (x, y and size)
* call you draw_sky function once...
* it should look something like this:

![lots of stars](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_4.png)

Extra Credit
-----
5 points

* within your draw sky function, increment the x value of every sub list by 1 as you iterate through the sub lists to draw stars
* instead of calling your draw_sky function once, use ontimer to have you draw_sky function call itself again in 30 ms
    * call ontimer at the end of your draw_sky function
    * with draw_sky as the first argument (no quotes), and 30 as the second
* you should see an animation!
* now... change your generate_star_data function so that the sub list that creates also contains a 4th value
    * this value represents a velocity
    * it should be small (maybe between 1 and 5)
* in your draw_sky function, as you iterate through your list of star data, add the generated velocity (the value at index 3) to the x value (the value at index 0) rather than just increment by 1

![animation](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/starry_ec.gif)
"""

import turtle
import random
wn = turtle.Screen()
t = turtle.Turtle()
width, height = 430, 320
wn.setup(width, height)
wn.tracer(0)
wn.bgcolor('black')
t.color('yellow')
top, bottom, left, right = height / 2, -height / 2, -width / 2, width / 2

X, Y, LENGTH, VELOCITY = 0, 1, 2, 3

def generate_star_data(n):
    stars = []
    for i in range(n):
        stars.append([random.randint(left, right), random.randint(bottom, top), random.randint(5, 60), random.randint(1, 4)])
    return stars

def draw_star(x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(5):
        t.forward(length)
        t.right(144)

def draw_sky():
    t.clear()
    for star in star_data:
        draw_star(star[X], star[Y], star[LENGTH])
        if star[X] >= width / 2:
            star[X] = (-width / 2) - star[LENGTH]
        else:
            star[X] += star[VELOCITY]
    wn.ontimer(draw_sky, 30)
    wn.update()

"""
# single star
draw_star(-200, 0, 400)
"""
"""
# 4 corners
size = 200
draw_star(left, top - size * 0.4, size)
draw_star(right - size * 1.2, top - size * 0.4, size)
draw_star(left, bottom + size * 0.8, size)
draw_star(right - size * 1.2, bottom + size * 0.8, size)
"""
"""
# row
for x in range(-400, 401, 50):
    draw_star(x, 0, 50)
"""
"""
# curve
t.up()
t.goto(left, bottom)
t.down
for i in range(20):
    draw_star(1.75 ** i - right, 30 * i ** 1.25 - top, i * 10)
"""
"""
# random
star_data = generate_star_data(40)
draw_sky()
"""
# animation
star_data = generate_star_data(20)
draw_sky()

wn.update()
wn.mainloop()
