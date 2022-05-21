a = int(input('Input number: '))
c = a
b = 0
while a > 0:
    b += a % 10
    a //= 10
print(f'Sum of digits of {c} is {b}')
