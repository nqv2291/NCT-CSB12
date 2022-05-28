lst = [5, 1, 8, 92, 7, 30]
eLST = []
for i in lst:
    if i%2 == 0:
        eLST.append(i)
print("Even numbers: ", end=" ")
for a in eLST:
    print(a, end=" ")