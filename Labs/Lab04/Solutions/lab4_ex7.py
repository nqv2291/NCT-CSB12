from turtle import *

shape('turtle')

# draw the curve
radius = 1
for i in range(20):  
  circle(radius, 180)
  radius += 10

mainloop()