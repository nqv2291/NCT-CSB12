import math
a= int(input("Input a: "))
b= int(input("input b: "))
c= int(input("Input c: "))
delta= (b**2)-(4*a*c)
if delta > 0:
    print("The equation has 2 solutions.")
    print("x= ",(-b - math.sqrt(delta)/ (2*a))," or ","x= ", (-b + math.sqrt(delta)/ (2*a)))
elif delta == 0:
    print("The equation has 1 solutions.")
    print("x= ",-b - math.sqrt(delta)/ (2*a))
else:
    print("The equation has no solutions.")
