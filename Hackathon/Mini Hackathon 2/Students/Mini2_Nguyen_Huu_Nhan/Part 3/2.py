list = ['5','1','8', '92', '-1', '30']
b = 0
print (list)
print (*list, sep = ", ")
for i in list:
    b += int(i)
print (f"Sum of all numbers: {b}")