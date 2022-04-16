from turtle import*

# #Part 1
# #1
# x = input("Input your name:")
# print(x)

# #2
# x = input("Input your name:")
# print(x.upper())

# #3
# x = int(input("Input a number:"))
# print(x*x)

# #4
# x = int(input("Input the radius:"))
# circle(x, 360)
# mainloop()

# #Part 2
# #1
# for i in range (3, 13):
#     print(i)

# #2
# x = int(input("Input a number:"))
# for i in range (0, x+1):
#     print(i)

# #3
# x = int(input("Input a number:"))
# t = x
# for i in range (0, x+1):
#     print(t)
#     t = t - 1

#4
x = int(input("Input number of edges:"))
y = (x-2)*180/x
for i in range (x):
    forward(100)
    left(180 - y)
    
mainloop()

#Part 3
#1
x = int(input("Input a number:"))
if x > 10:
    print("The number is higher than 10")
else:
    print("The number is lower than 10")

#2
x = int(input("Input a number:"))
if x % 2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")

#3
x = int(input("Input a month:"))
if x == 1:
    print("31")
elif x == 2:
    print("28, 29 if the year is divided by 4")
elif x == 3:
    print("31")
elif x == 4:
    print("30")
elif x == 5:
    print("31")
elif x == 6:
    print("30")
elif x == 7:
    print("31")
elif x == 8:
    print("31")
elif x == 9:
    print("30")
elif x == 10:
    print("31")
elif x == 11:
    print("30")
elif x == 12:
    print("31")

