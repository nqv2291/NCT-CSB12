color = ["blue","red","green"]
print('Danh sách màu: ')
for i in range(0,len(color)):
    print(color[i],end=" ")
New = input("Thêm màu mới: ")
color.append(New)
for i in range(0,len(color)):
    print(color[i],end=" ")