# calculate factorial of a number
def fac(num):
    factorial = 1

    # trivial case
    if num < 2:
        return factorial

    # normal case
    for i in range(2, num+1):
        factorial *= i
    return factorial

# calculate expression
# trick: 1!/1 + 2!/2 + ... + n!/n = 0! + 1! + ... + (n-1)!
def cal_formula(n):
    sum = 0
    for i in range(n):
        sum += fac(i)
    return sum

# get input
n = int(input("Input number: "))

# print result
print(f"Result: {cal_formula(n)}")