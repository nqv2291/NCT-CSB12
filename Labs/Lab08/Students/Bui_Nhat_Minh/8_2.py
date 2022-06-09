def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input('Input number: '))
if (is_prime(n)):
    print(f'{n} is a prime')
else:
    print(f'{n} is not a prime')
