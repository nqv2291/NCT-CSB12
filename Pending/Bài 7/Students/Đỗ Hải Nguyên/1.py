
color=["blue","red","green"]
print('corlor list:')
for i in range(0,len(color)):
    print(color[i],end=", " )
New=input("input new color: ")
color.append(New)
for i in range(0,len(color)):
    print(color[i],end=", " )
