import turtle
t = turtle.Turtle()

a = 5

for i in range(20):
    t.circle(a,90)
    a += 5

turtle.exitonclick()