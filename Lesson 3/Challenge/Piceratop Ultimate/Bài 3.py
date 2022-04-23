import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = b * b - 4 * a * c
if d < 0:
    print('The equation has no solution!!')
elif d > 0:
    print('Solution:')
    print(f' x1 = {(-b+math.sqrt(d))/2/a}')
    print(f' x2 = {(-b-math.sqrt(d))/2/a}')
else:
    print(f'root = {-b/2/a}')
