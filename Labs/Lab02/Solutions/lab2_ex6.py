from turtle import *

# define sizes
rect_edge1 = 150
rect_edge2 = 120
triangle_edge = (rect_edge1/2) * 2**(1/2)  # Pythagore

shape('turtle')

speed(1)
# draw rectangle
forward(rect_edge1)
left(90)
forward(rect_edge2)
left(90)
forward(rect_edge1)
left(90)
forward(rect_edge2)

# draw triangle & red lines
pensize(10)
pencolor('#de5246')


backward(rect_edge2)
left(45)
forward(triangle_edge)
left(90)
forward(triangle_edge)
right(135)
forward(rect_edge2)

# move turtle to top
penup()
right(90)
forward(rect_edge1/2)
right(90)
forward(rect_edge2*1.2)

mainloop()