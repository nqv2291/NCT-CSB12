import turtle
lst = ["blue", "red", "yellow", "green"]
turtle.width(5)
turtle.shape("turtle")
for i in lst:
    turtle.pencolor(i)
    turtle.forward(20)
    turtle.pencolor('white')
    turtle.forward(20)
turtle.done()