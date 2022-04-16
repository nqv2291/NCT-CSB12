# return factorial of a number
def fact(num):
    fac = 1  
    for i in range(1, num+1):
        fac *= i
    return fac

# get input
num = int(input("Enter a number: "))

# print num!
print(f"Factorial: {num}! = {fact(num)}")
