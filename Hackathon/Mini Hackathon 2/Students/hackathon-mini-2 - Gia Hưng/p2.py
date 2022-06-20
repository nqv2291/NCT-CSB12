colorlist = [ "red" , "blue" , "green"]
number = int(input("enter position"))
print(colorlist[number])
dele = input("color you want to delete")
if(dele.isnumeric() == True):
    numdele = int(dele)
    del(colorlist[numdele])
else:
    colorlist.remove(dele)
print(colorlist)
from shutil import which
import turtle

colorlist2 = ["red" , "orange" , "yellow" , "green" , "blue" , "violet"]
from turtle import *
for i in colorlist2:
    turtle.color(i)
    forward(50)
    penup()
    forward(50)
    pendown()
mainloop()