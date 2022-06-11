n = int(input("Please input a number: "))

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

if isPrime(n):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')
