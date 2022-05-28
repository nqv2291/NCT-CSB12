import turtle
turtle.shape("turtle")
lst = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
turtle.pensize(5)
for i in lst:
    turtle.pencolor("white")
    turtle.forward(40)
    turtle.pencolor(i)
    turtle.forward(50)
turtle.pencolor("white")
turtle.forward(40)

turtle.exitonclick()



