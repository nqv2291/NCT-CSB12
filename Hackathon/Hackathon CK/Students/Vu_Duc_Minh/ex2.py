import math

a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))
c = float(input("Please enter the third number: "))

if (a == 0):
    if (b == 0):
        print ("No solutions");
    else:
        print ("1 Solution: x = ", + (-c / b));

delta = b * b - 4 * a * c;


if (delta > 0):
    x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
    x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
    print ("2 Solutions: x1 = ", x1, " và x2 = ", x2);
elif (delta == 0):
    x1 = (-b / (2 * a));
    print("1 Duplicate Solution: x1 = x2 = ", x1);
else:
    print("No solutions.");