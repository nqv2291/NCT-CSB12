from turtle import *

shape('turtle')
pensize(10)

# draw first shape
pencolor('#cf8f03')
left(30)
forward(100)
right(60)
forward(100)
right(120)
forward(100)
right(60)
forward(100)

# move to next shape
penup()
right(150)
forward(50)
pendown()

# draw second shape
pencolor('#0b2c3c')
left(30)
forward(100)
right(60)
forward(100)
right(120)
forward(100)
right(60)
forward(100)

mainloop()