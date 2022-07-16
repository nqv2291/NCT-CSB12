import math

while True:
    try:
        a = float(input('Input a: '))
        if (a == 0):
            raise Exception('Please pick a different value for a.')
        b = float(input('Input b: '))
        c = float(input('Input c: '))
    except Exception as e:
        if str(e) == 'Please pick a different value for a.':
            print(str(e))
        else:
            print('Numbers only, please.')
        continue
    else:
        break

delta = b*b - 4*a*c
if delta < 0:
    print('The equation has 0 solution.')
elif delta == 0:
    print('The equation has 1 solution.')
    print(f'x = {-b/(2*a)}')
else:
    print('The equation has 2 solutions.')
    print(
        f'x = {(-b-math.sqrt(delta))/2/a}    or    x = {(-b+math.sqrt(delta))/2/a}')
