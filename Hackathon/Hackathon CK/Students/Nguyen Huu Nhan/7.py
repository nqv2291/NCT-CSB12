list1 = [5,1,8,92,-1,30]
list2 = []
for i in range(len(list1)):
    for b in range(i+1, len(list1)):
        if list1[i] > list1[b]:
            list1[i], list1[b] = list1[b], list1[i]
            print (list1 )
print (list1)
