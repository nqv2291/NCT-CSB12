n = int(input('Input a number: '))
if n == 2:
    print('This month has 28 days')
elif n == 4 or n == 6 or n == 9 or n == 11:
    print('This month has 30 days')
else:
    print('This month has 31 days')
