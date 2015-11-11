"""
your_face.py (5 points)
=====
Draw a face using turtle. For example, you can draw the look of disapproval!

![look of disapproval](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/your_face.png)

Requirements
-----

* you can draw whatever face you like
* but you have to use the turtle module
    * change the size of the pen 
    * set the window size to 400 x 400
    * turn animation off (for sanity's sake)
* create a function called draw_face ... it's up to you to decide if it should have parameters or not (it's ok if you don't parametrize it, but it may be helpful for extra credit)
    * your function will draw a face
    * use at least one circle
    * use at least one line
    * remember to call update at the end of your function to let Python know to _repaint_ the screen
* call your function at the end of your program

Extra Credit
-----
5 points (warning: this is one may be a little frustrating depending on how complicated your drawing is!)

* ask the user for comma separated input that specifies how to draw the face... with each value representing x, y and size respectively
    * for example, 0,0,20 means draw the face at (0, 0) with size 20
    * size can mean whatever you like... 
* using the string method, split, break up the input, and use each individual value to draw the face
* continue to ask for input, with each new input drawing another face
* hints:
    * how do you keep the relationship between all of the parts of the face in proportion?
    * setheading might be helpful
* see the example below:

![asking for input](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/your_face_ec.gif)

"""
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)
wn.setup(500,500)
t.pensize(5)
t.hideturtle()


def draw_eye(x, y, size):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    r = size
    r2 = size / 5
    t.circle(r)
    t.setheading(90)
    t.up()
    t.forward(r - r2)
    t.down()
    t.setheading(0)
    t.circle(r2)
    t.setheading(90)
    t.up()
    t.forward(r * 2 - (r - r2))
    t.setheading(0)
    t.back(r * 2 - (r - r2))
    t.down()
    t.forward(r * 2.5)
    t.left(135)
    t.forward(r)

def draw_face(x, y, size):
    draw_eye(x, y, size)
    eye_to_eye = size * 5
    draw_eye(x + eye_to_eye, y, size)
    mouth_width = size * 1.5
    t.up()
    t.goto(x + eye_to_eye / 2 - mouth_width / 2, y - mouth_width / 2)
    t.down()
    t.setheading(0)
    t.forward(mouth_width)
    wn.update()


#x, y, s = int(input('x?\n> ')), int(input('y?\n> ')), int(input('size?\n> '))

#draw_face(0, 0, 20)
print('\n\n\n\n\n')
while True:
    answer = input('x,y,size?\n> ')
    parts = answer.split(',')
    #print(parts)
    x, y, s = int(parts[0]), int(parts[1]), int(parts[2])
    draw_face(x, y, s)
wn.update()
wn.mainloop()
