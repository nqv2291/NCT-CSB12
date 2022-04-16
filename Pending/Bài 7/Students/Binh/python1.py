#Bai 2
list = ["blue", "red", "teal", "green"]

print(*list, sep = ", ")




#Bai 3
list = ["blue", "red", "teal", "green"]


print(f'Current Fruits List ', *list, sep = ",")

f = input("New color list: ")
list.append(f)

print(f'Updated Fruits List: ', *list, sep = ",")