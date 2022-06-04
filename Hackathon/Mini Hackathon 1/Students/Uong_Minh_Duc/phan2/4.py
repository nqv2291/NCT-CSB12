 import turtle
 t=turtle.Turtle()
 side=int(input("side number:"))
 for _ in range(50):
     turtle.forward(50)
     turtle.right(360/side)
