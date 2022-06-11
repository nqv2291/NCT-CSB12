def isPrime(n):
    if n==2 or n==3: 
        return True
    if n%2==0 or n<2: 
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def primePrinter(n):
    i = 2
    while n > 0:
        if isPrime(i):
            print(f' {i}', end="")
            n -= 1
        i += 1


n = int(input('Input number: '))
print(f'First {n} prime(s):', end='')
primePrinter(n)