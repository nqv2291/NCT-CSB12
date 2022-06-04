#input num
n = int(input("Input number of edges: "))
l = 100

import turtle
turtle.shape("turtle")

# set turtle
t=turtle.Turtle()

#loop
for i in range(n):
    t.forward(l)
    t.right(360/n)
turtle.exitonclick()