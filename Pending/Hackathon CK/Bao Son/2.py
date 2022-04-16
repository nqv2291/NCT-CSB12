import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a == 0:
    print(int(input("Nhập lại a khác 0: ")))

delta = b*b - 4*a*c

if delta < 0:
    print('Phương trình vô nghiệm')
elif delta == 0:
    print('Phương trình có nghiệm kép x1 = x2 =', -b/2*a)
else:
    if a == 0:
        print('Phương trình có vô số nghiệm')
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print('Phương trình có 2 nghiệm phân biệt: ', x1, 'và', x2)