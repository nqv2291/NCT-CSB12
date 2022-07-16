import math
a = float(input("Input a: "))
b= float(input("Input b: "))
c= float(input("Input c: "))

if (a == 0):
    if (b == 0):
        print ("No solution")
    else:
        print ("One solution: x = ", + (-c / b))

delta = b * b - 4 * a * c

if (delta > 0):
    x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
    x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
    print ("Two solutions: ")
    print("x =", x1, "or", "x", x2 )
elif (delta == 0):
    x1 = (-b / (2 * a))
    print("Two same solutions: x1 = x2 = ", x1)
else:
    print("No solution");


