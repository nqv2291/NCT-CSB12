# return fibonacci sequence
def print_fibo(n):
    fibo = [0, 1]

    for i in range(n):
        if i >= 2:
            fibo.append(fibo[i - 1] + fibo[i - 2])
        print(fibo[i], end=" ")
    print()

# get input
n = int(input("Enter a number: "))

# print fibonacci sequence
print(f"First {n} element(s) of fibonacci sequence: ", end=" ")
print_fibo(n)
