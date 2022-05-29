list1 = [78, 56, 67]
print ("High score:")
for i in range (len(list1)):
    print (f"{i+1}. {list1[i]}")
new = input ("A new score:")
list1.append(new)
print ("High score:")
for i in range (len(list1)):
    print (f"{i+1}. {list1[i]}")