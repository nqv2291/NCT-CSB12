import turtle
t = turtle.Turtle()
turtle.shape('turtle')
n = int(input("Number of edges: "))
l = 100
for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
turtle.done()