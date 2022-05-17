print(3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

number = int(input("enter your number"))
for i in range(0 , number + 1):
    print(i , end = "")

print("")

number2 = int(input("enter another number"))
for i in range(1 , number2 + 1 ):
    if(i%2!= 0 ):
        print(i , end= "")

print("")

edge = int(input("number of edge"))
corner = 360/edge
from turtle import *
for i in range(edge):
    forward(100)
    left(corner)
mainloop()