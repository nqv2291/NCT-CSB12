# 2.1
def factorial(n):
    if n < 0: 
        return "undefined"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input('Input a number: '))
print(f"{n}! = {factorial(n)}")
# 2.2
list_num = [5,1,8,92,-1,30]
def listSorter(n):
    list2 = []
    while n:
        min = n[0]
        for i in n:
            if i < min:
                min = i
        list2.append(min)
        n.remove(min)
    return list2
print(f'Pre-sorted list: {list_num}')
print(f'Sorted list: {listSorter(list_num)}')
# 2.3
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