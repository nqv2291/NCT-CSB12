import math

# check for prime number
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

# print sequence of prime number
def prime_sequence(n):
    print(f"First {n} prime(s): ", end=" ")
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

# get input
n = int(input("Input number: "))

# print result
prime_sequence(n)
