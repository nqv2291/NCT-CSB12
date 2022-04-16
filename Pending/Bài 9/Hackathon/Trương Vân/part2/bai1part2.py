#funtion to cal factorial
def fac(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num = int(input("input a positive integer:  "))
print(f"factorial of {num} is {fac(num)}")    