#bai 1

# a = int(input("write a: "))
# b = int(input("write b: "))
# c = int(input("write c: "))

# if (a >= b) and (a >= c):
#     largest = a
# elif (b >= a) and (b >= c):
#     largest = b
# else:
#     largest = c

# print(f"Largest number is: {largest}")

#bai2

d = int(input("write a year have 4 number: "))

if (d%100 == 0 ) or (d%4 == 0):
    print(f"{d} is a leap year")
else:
    print(f"{d} is not a leap year")