#cách 1 
n = int(input("Input number: "))
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"{int(n)} is a prime")
    else:     
        print(f"{n} is not a prime")
is_prime(n)
#cách 2 
def is_prime(num):
    if num == 1:
        print("1 is not a prime")
    else:
        for x in range(2,num):
            if num % x == 0:
                print(f'{num} is not a prime')
                exit()
        
        print(f"{num} is a prime")
#check
num = int(input("input number:  "))
is_prime(num)

