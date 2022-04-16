
from tkinter import Y


prc = {
    'ASUS': '400',
    'DELL': '650'
}
d =(input("Input a brand: "))
v =(input("Input amount to buy: "))
v = int(v)
if d == ('DELL'):
  print("Total price :", v * 650 )
else:
    print("Total price :", v * 400)

