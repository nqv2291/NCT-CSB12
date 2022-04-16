def is_prime(n):
    if n == 2:
        return True
    else:    
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
num = int(input("Input number: "))
k = 0
list_numbers = []
s = 1
while k < num:
    if is_prime(s):
        list_numbers.append(s)
        k+=1
        s+=1
    else:
        s+=1
print(f'First {num} prime numbers: ')
for i in list_numbers:
    print(i, end= " ")
