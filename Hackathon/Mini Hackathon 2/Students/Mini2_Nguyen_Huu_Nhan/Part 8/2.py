list1 = [78, 56, 67]
list1.sort(reverse=True)
print ("High score:")
for i in range (len(list1)):
    print (f"{i+1}. {list1[i]}")
new = int(input ("A new score:"))
list1.append(new)
list1.sort(reverse=True)
print ("High score:")
for i in range (len(list1)):
    print (f"{i+1}. {list1[i]}")