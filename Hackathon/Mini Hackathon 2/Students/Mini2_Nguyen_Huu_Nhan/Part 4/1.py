list = ['5','1','8', '92', '-1', '30']
for i in list:
    if i % 2 != 0:
        del(list[i])
    else:
        continue
print ("Even numbers:")
print (*list, sep = ", ")