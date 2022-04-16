import math
a=int(input("input a: "))
b=int(input("input b: "))
c=int(input("input c: "))

denta=b*b+4*a*c

if a==0:
    print("invalid")
elif denta<0:
    print("Vo nghiem")
elif denta==0:
    print("phuong trinh co 1 nghiem kep:",(-b)/(2*a))
else:
    print(f"phuong trinh co 2 nghiem phan biet x1={(-b + math.sqrt(denta))/(2*a)} x2= {(-b - math.sqrt(denta))/(2*a)}")