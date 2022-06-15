def factorial(s: int):
    fact = 1
    for i in range(1, s+1):
        fact *= i
    return fact
s = int(input('Input a number: '))
print(f"{s}! = {factorial(s)}")