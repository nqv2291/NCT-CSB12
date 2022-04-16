a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))
from math import *
delta = b**2 - 4*a*c
if delta > 0:
    print("this equation has 2 solutions")
    print("x =",(-b+sqrt(delta)/2*a),"or x =",(-b-sqrt(delta)/2*a))
else: 
    print("this equation has no solutions")
