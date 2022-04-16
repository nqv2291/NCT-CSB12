def is_prime(n):
    if n == 2:
        return True
    else:    
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True

num = int(input("Enter a positive integer: "))
if is_prime(num):
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime") 
