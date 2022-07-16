import math

a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

if (a == 0):
    if (b == 0):
        print ("The equation has no solution")
    else:
        print ("The equation has 1 solution: x = ", + (-c / b))


delta = b * b - 4 * a * c

if (delta > 0):
    x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
    x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
    print ("The equation has 2 solutions: x1 = ", x1, " và x2 = ", x2)
elif (delta == 0):
    x1 = (-b / (2 * a))
    print("The equation has double solution: x1 = x2 = ", x1)
else:
    print("The equation has no solution")

