# #bài 1
# full_name = input("enter full name: ")
# print("hello, ", full_name)
# #bài 2
# smth = input("enter something: ")
# print(smth.upper()) 
# #bài 3
# x = float(input("enter a number: "))
# print(x**2)
#bài 4
from turtle import *
radius = float(input("input radius: "))
from turtle import *
if radius <= 0:
    print("re-enter radius please")
else: 
    circle(radius)
mainloop()