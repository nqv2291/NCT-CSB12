# Cau 1
# def is_int(n):
#     if isinstance(n, int):
#         return True
#     if isinstance(n, float):
#         return n.is_integer()
#     return False
# num = float(input("Input number: "))
# is_int(num)
# if is_int(num):
#     print(f'{int(num)} is an integer')
# else:
#     print(f'{num} is not an integer')

# Cau 2
def PrimeChecker(a):  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
        else:  
            print(a, "is a prime number")  
    else:  
        print(a, "is not a prime number")  
a = int(input("Enter an input number:"))  
PrimeChecker(a)  

# Cau 3
# n = int(input("Input number: "))
# p = [2]
# c = 2

# while len(p) < n:
#     j = 0
#     c = c + 1
#     while j < len(p):
#         if c % p[j] == 0:
#             break
#         elif j == len(p) - 1:
#             p.append(c)
#         j += 1
# print(f"First {n} prime(s): {p}")

# Cau 4
# import math
# num = int(input("Input number: "))
# op = math.factorial(num)/num
# a = 1
# for i in range(1, num+1):
#     a = a * i
# print(op)

# Cau 5
from datetime import datetime
now = datetime.now()
print("Today is", now.strftime('%Y/%m/%d'))
print("Time right now:", now.strftime('%H:%M:%S'))