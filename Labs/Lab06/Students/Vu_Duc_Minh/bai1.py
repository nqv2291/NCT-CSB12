lst = [0,1,2,3,4,5,6,7,8,9]
res = []
res2 = []
res3 = lst
for i in lst:
    res.append(i + 2)
    res2.append(i * 2)
for x in range(2):
    ie = lst.pop(0)
    lst.append(ie)
print ("+2 list is : " + str(res))
print ("x2 list is : " + str(res2))
print("shift 2 list is: " + str(res3))