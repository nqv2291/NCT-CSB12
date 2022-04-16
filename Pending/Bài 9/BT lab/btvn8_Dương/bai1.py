def is_int(n):
    if n == int(n):
        return True

num = float(input("Enter a real number: "))
if is_int(num):
    print(f'{int(num)} is an integer')
else:
    print(f'{num} is not an integer')