print("""Input the list of numbers.
Enter 0 to finish.""")

lst = []
a = int(input())
lst.append(a)
while a != 0:
    a = int(input())
    lst.append(a)

Sum = sum(lst)
print(Sum)