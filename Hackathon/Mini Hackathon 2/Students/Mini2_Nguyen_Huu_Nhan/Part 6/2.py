list1  = ['BĐ', 'BTL', 'CG9', 'ĐĐ', 'HBT']
list2 = [247100 , 333300 ,266800 ,420900, 318000]
list3 = [9.224, 43.35,12.04,9.96,10.09] 
b = 0
for i in range(len(list1)):
    b = list2[i] / list3[i] + b
print (f"Average population density {b/ len(list1)}")