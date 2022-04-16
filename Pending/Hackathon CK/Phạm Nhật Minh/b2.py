from math import *
print("Giai phuong trinh bac 2: ax^2+bx+c")
a=float(input("Nhap so a:"))
while True:
    if a==0:
        print("a la so khac 0, moi nhap lai.")
        a=float(input("Nhap so a:"))
        continue
    if a!=0:
        break
b=float(input("Nhap so b:"))
c=float(input("Nhap so c:"))
delta=b**2-4*a*c
if delta>0:
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    print("Phuong trinh co 2 nghiem")
    print(f"x1={x1} or x2={x2}")
elif delta==0:
    x12=-b/2*a
    print(f"Phuong trinh co nghiem kep x={x12}")
else:
    print("Phuong trinh vo nghiem")