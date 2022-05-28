arr =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = arr.copy()
l2 = arr.copy()
l3 = arr.copy()
for i in range(len(l1)):
    l1[i] += 2
print(l1)
for i in range(len(l2)):
    l2[i] *= 2
print(l2)
list = l3[-8:] + l3[:-8] 
print (str(list))