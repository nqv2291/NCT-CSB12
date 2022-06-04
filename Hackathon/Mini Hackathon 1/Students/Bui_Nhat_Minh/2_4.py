import turtle
e = int(input('Input number of edges: '))
for i in range(e):
    turtle.forward(50)
    turtle.left(360/e)
turtle.done()
