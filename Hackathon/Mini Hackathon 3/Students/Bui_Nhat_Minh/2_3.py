fibo_arr = [1, 1]


def add_fibo_nth_term(n):
    if len(fibo_arr) < n:
        add_fibo_nth_term(n-1)
        fibo_arr.append(fibo_arr[-1] + fibo_arr[-2])


def print_fibo(n):
    add_fibo_nth_term(n)
    print(f'First {n} Fibonacci numbers:', end=" ")
    for i in range(n):
        print(fibo_arr[i], end=' ')
    print()


n = int(input('Input a number: '))
print_fibo(n)
