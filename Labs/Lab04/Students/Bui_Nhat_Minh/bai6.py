import turtle
a = int(input('Input number of edges: '))
b = 360 / a
for i in range(a):
    turtle.forward(100)
    turtle.right(b)
turtle.done()
