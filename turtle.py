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

  for i in range(8):
  
    if i % 2 == 0:
      color('maroon')
    else:
      color('firebrick')
      
    forward(70)
    right(45)




