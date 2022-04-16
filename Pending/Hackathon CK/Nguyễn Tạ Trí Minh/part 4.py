from random import choices
from secrets import choice
from tkinter import Y, Menu


menulist =[]
while True:
    order= input("Please choose a dish: ")
    if order in menulist:
      print("You chose this already. ")
      choices2=input("Anything else?(y/n)")
      if choices2 == "n":
        print("Well done! Your order:",menulist)
        break
    elif order not in menulist:
     menulist.append(order)
     choices=input("Great choice! Anything else? (y/n): ")
     if choices == "n":
        print("Well done! Your order:",menulist)
        break
  

    
    
