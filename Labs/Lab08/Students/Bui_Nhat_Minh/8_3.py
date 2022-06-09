def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def print_prime_numbers(n):
    start_prime = 2
    while n > 0:
        if is_prime(start_prime):
            print(f' {start_prime}', end='')
            n -= 1
        start_prime += 1


n = int(input('Input number: '))
print(f'First {n} prime(s):', end='')
print_prime_numbers(n)
