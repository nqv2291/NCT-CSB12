print ("""Input the list of numbers.
Enter 0 to finish.""")
list = []
list2 = []
b = 0
while True:
    inpu = int(input(""))
    list.append(inpu)
    if inpu == 0:
        break
for i in list:
    if i % 2 == 0:
        list2.append(i)
    else:
        continue
list2.pop()
print ("Even numbers:")
print (*list2, sep = ", ")
