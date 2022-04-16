from turtle import*

import turtle



#Part 1

a = ["red", "blue", "green"]

print("Color list: ", a)

x= input("Input a new color:")

a.append(x)

print("Color list: ", a)



#Part 2

a = ["red", "blue", "green"]

print("Color list: ", a)

x= int(input("Input position:"))

print("Color at position:", a[x-1])

y= input("Item to delete:")

a.remove(y)

print("New color list:", a)

for i in a:

    color(i)

    forward(100)

    



#Part 3

a = [5, 1, 8, 92, -1, 30]

x = int(input("Input a number:"))

if x in a:

    print("Number found at position", a.index(x)+1)

else:

    print("Number not found")



#Part 4

a = [5, 1, 8, 92, 7, 30]

for i in a:

    if (i % 2 == 0):

        print("Even numbers:", i)



y = []

while True:

    x= int(input())

    print(x)

    y.append(x)

    if (x == 0):

        break



for i in y:

    if (i % 2 == 0):

        print("Even number in list:", i)