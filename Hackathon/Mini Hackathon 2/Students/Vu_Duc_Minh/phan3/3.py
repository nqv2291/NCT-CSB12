a = int(input("Please input the list of numbers, enter 0 to finish: "))
lst = []
b=0
while a != 0:
    lst.append(a)
    a = int(input())
    for i in lst:
        b += i
print("Sum of all number(s):",b)