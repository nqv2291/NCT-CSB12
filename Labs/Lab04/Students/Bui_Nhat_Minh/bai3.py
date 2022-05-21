a = int(input('Input number: '))
if (a < 0):
    print('Invalid')
else:
    b = 1
    for i in range(1, a + 1):
        b *= i
    print(f'{a}! = {b}')
