arr = [0,1,2,3,4,5,6,7,8,9]
lst = arr.copy()
lst2 = arr.copy()

#add 2
arr2 = []
for i in lst:
    if i >= 2:
        arr2.append(i)
print(f"Add 2         : {arr2}")


#muiltiply 2
arr3 = []
for a in lst:
    a = a * 2
    arr3.append(a)
print(f"Multiply by 2 : {arr3}")


#shift 2
lst2.remove(0)
lst2.remove(1)
lst2.extend(    [0,1]    )
print(f"Shift 2       : {lst2}")

