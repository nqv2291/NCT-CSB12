from turtle import *
import math

#ve hinh vuong
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

#di chuyen ve hinh thoi
up()
setpos(50,50)
left(90)
forward(50*math.sqrt(2))
down()

#ve hinh thoi
left(135)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

#di chuyen ve trung tam
right(45)
up()
setpos(50,50)
down()
shape("turtle")

mainloop()