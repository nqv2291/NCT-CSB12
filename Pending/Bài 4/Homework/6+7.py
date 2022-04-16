from turtle import *
from math import*
a=float(input('input length 1: '))
b=float(input('input length 2: '))
c=float(input('input length 3: '))
conclution=str('đây là độ dàu 3 cạnh của tam giác')
if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        conclution= conclution + " đều "
    elif a==c!=b  or b==c!=a   or a==b!=c   :
        conclution= conclution + " cân "
    elif a**2==b**2+c**2 or b**2==c**2+a**2 or c**2==a**2+b**2:
        conclution=conclution+ " vuông "
    else:
        conclution=conclution+ " thường "
else:
    print("đây khổng phải là độ dài 3 cạnh của tam giác")
    quit()
print(conclution)
forward(c)
left(180-degrees(acos((a**2+c**2-b**2)/(2*a*c))))
forward(a)
left(180-degrees(acos((b**2+a**2-c**2)/(2*b*a))))
forward(b)
mainloop()