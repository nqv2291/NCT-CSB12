n = int(input('Input a positive number: '))
arr = []
for i in range(n):
    if i == 0 or i == 1:
        arr.append(1)
    else:
        arr.append(arr[i-1] + arr[i-2])
print(f'First {n} Fibonacci number(s):', end=' ')
for i in range(n):
    print(arr[i], end=' ')
