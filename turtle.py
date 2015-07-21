# turtle is a way to do graphics


from turtle import *


from turtle import *

shape('turtle')
color('#31B404')

# draw a square

for i in range(4):
  forward(100)
  right(90)


# draw an octagon with alternation colors

from turtle import *

  for i in range(8):
  
    if i % 2 == 0:
      color('maroon')
    else:
      color('firebrick')
      
    forward(70)
    right(45)

# add multiple turtles / beatles

from turtle import *

john = Turtle()
paul = Turtle()
george = Turtle()
ringo = Turtle()

john.shape('circle')
paul.shape('triangle')
george.shape('square')
ringo.shape('turtle')

john.color('red')
paul.color('yellow')
george.color('green')
ringo.color('blue')

john.goto(50,50)
paul.goto(-50, 50)
george.goto(50,-50)
ringo.goto(-50, 50)





