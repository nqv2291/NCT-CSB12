def print_fibo(n):
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return print_fibo(n - 1) + print_fibo(n - 2)

n = int(input('Input a number: '))
print(f'First {n} Fibonacci number(s): ', end='')
for i in range(1, n+1):
    print(print_fibo(i), end=" ")