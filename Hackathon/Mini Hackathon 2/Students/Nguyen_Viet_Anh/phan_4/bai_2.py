print("""Input the list of numbers.
Enter 0 to finish.""")

lst = []
a = int(input())
lst.append(a)
while a != 0:
    a = int(input())
    lst.append(a)

eLST = []
for i in lst:
    if i%2 == 0:
        eLST.append(i)
print("Even numbers: ", end=" ") 
eLST.remove(0)
for a in eLST:
    print(a, end=" ")