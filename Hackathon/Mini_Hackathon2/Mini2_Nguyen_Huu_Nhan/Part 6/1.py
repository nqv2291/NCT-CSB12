list1  = ['BĐ', 'BTL', 'CG9', 'ĐĐ', 'HBT']
list2 = [247100 , 333300 ,266800 ,420900, 318000]
list3 = [9.224, 43.35,12.04,9.96,10.09] 
for i in range(len(list1)):
    print (f"{list1[i]}: {float(list2[i] / list3[i])}")