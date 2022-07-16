import math
print("ax^2 + bx + c")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
delta = b^2 - 4*a*c


if(delta < 0):
    print("Undefined x")

elif(delta == 0):
    x = -1*b / 2*a
    print(f"The equation have 1 solution: {x}")
else:
    sqdelta = math.sqrt(delta)
    x1 = -1*b + sqdelta / 2*a
    x2 = -1*b - sqdelta / 2*a
    print(f"The equation have 2 solution: {x1} and {x2}")

