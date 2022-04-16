import turtle
x=int(input("input number of edges: "))
while x<=2:
    x=int(input("input number of edges: "))
a=((x-2)*180)/x
for i in range(x):
    turtle.forward(200)
    turtle.left(180-a)
turtle.mainloop()