import turtle
n = int(input("Please input the amount of edges you want the turtle to draw: "))
l = 50
while n <= 2:
    print("Please try again.")
    n = int(input("Please input the amount of edges you want the turtle to draw: "))
if n > 2:
    for x in range(n):
        turtle.forward(l)
        turtle.right(360/n)
    turtle.done()