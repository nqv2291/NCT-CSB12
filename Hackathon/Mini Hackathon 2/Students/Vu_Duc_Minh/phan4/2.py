a = int(input("Please input the list of numbers, enter 0 to finish: "))
lst = []
while a != 0:
    lst.append(a)
    a = int(input())
print("Even numbers in list:")
for i in lst:
    if i % 2 == 0:
        print(i, end=" ")