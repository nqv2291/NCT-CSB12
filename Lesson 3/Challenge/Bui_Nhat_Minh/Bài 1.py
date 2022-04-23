a = float(input('Number 1: '))
b = float(input('Number 2: '))
c = float(input('Number 3: '))
if b > a:
    a = b
if c > a:
    a = c
print(f'The largest number is {a}')
