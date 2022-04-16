def is_int(num):
    return num % 1 == 0
a=input('input number: ')
a=float(a)
if is_int(a):
    print(f'{int(a)} is an integer')
else:
    print(f'{a} is not an integer')
