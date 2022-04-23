import math
# Ex 1
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if (a >= b and a >= c):
    print("The largest number is", a)
elif (b >= a and b >= c):
    print("The largest number is", b)
else:
    print("The largest number is", c)
# Ex 2
cen_year = 0
year = int(input("Enter year: "))
if year % 100 == 0:
    cen_year = year
    if cen_year % 400 == 0:
        print(f"{cen_year} is a leap year")
    else:
        print(f"{cen_year} is not a leap year")
else:
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
# Ex 3
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if (a == 0):
    if (b == 0):
        print("The equation has no solution!")
    else:
        print(f"Solution: x = {-c / b}")
else:
    delta = b ** 2 - 4 * a * c
    if (delta > 0):
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        print(f"Solutions: x1 = {x1}, and x2 = {x2}")
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print(f"Solutions: x1 = x2 = {x1} ")
    else:
        print("The equation has no solution!")
