
def factorial_array(n):
    factorial_number = [1]
    for i in range(1, n):
        factorial_number.append(i * factorial_number[i - 1])
    return factorial_number


n = int(input('Input number: '))
arr = factorial_array(n)
print(f'Result: {sum(arr)}')
