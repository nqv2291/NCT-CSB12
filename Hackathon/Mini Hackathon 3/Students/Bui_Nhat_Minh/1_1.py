def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Input a number: '))
if check_even(n):
    print('This number is even')
else:
    print('This number is not even')
