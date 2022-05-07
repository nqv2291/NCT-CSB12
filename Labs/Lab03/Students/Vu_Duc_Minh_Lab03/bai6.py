a = int(input("Please input a number for triangle length 1: "))
b = int(input("Please input a number for triangle length 2: "))
c = int(input("Please input a number for triangle length 3: "))
ab = int(a+b)
bc = int(b+c)
ac = int(a+c)
if (ab > c) and (bc > a) and (ac > b):
    print("These 3 numbers are compatible to form a triangle")
else:
    print("These 3 numbers are not compatible to form a triangle")