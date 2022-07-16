import math
a = int(input('Input a'))
b = int(input('Input b'))
c = int(input('Input c'))  
delt = (b**2) - (4*a*c)
if delt > 0:
    print("The equation has 2 solutions")
    print (f"x={(-b-math.sqrt(delt))/(2*a)} or x = {(-b+math.sqrt(delt))/(2*a)}")
elif delt == 0:
    print ("The equation has 1 solution")
    print(f"x={-b/(2*a)}")
else:
    print("no solution")

