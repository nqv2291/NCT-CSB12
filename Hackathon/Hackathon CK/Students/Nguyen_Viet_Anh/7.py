lst = [5, 1, 8, 92, -1, 30]

print("Original list:")
for i in lst:
    print(i,end=" ") 

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            
print("")
print("Sorted list: ")
for i in lst:
    print (i,end=" ")