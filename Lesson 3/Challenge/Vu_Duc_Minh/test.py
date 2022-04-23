#Bài 1
a = int(input("Please input a number"))
b = int(input("Please input a number"))
c = int(input("Please input a number"))

if (a > b) and (a > c):
    print(a, "is the largest number")
elif (b > a) and (b > c):
    print(b, "is the largest number")
elif (c > a) and (c > b):
    print(c, "is the largest number")
else:
    print("every number is equal")

#Bài 2
# a = int(input("You can input a year:"))
# b = a % 4
# if b == 0:
#     print(a, "is a leap year")
# else:
#     print(a, "is not a leap year")