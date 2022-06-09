def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

n = input("Input number: ")
if is_int(n):
    print(f'{n} is an integer')
else:
    print(f'{n} is not an integer')