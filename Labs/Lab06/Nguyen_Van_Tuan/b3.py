nums = int(input("Input a positive number: "))
arr = []
for i in range(nums):
    if i == 0 or i == 1:
        arr.append(1)
    else:
        arr.append(arr[i-1] + arr[i-2])
print(f'First {nums} Fibonacci number(s):', end=' ')
for i in range(nums):
    print(arr[i], end=' ')
