a = int(input("put a positive num90er > 2: "))
b = 120

import turtle
t = turtle.Turtle()
t.speed(2)
if(a == 3):
    for i in range(a):
        t.forward(90)
        t.right(b)
        
elif(a == 4):
    for i in range(a):
        t.forward(90)
        t.right(90)
elif(a == 6):
    for i in range(a):
        t.forward(90)
        t.right(60)
else:
    print("co cai nit")
    


turtle.exitonclick()