lst = ["Blue", "Green", "Purple", "Gray"]

print("Color list: ")
for i in lst:
    print(i,end=" ")

print("")
print("Input new color: ",end="")

int = input()
lst.append(int)

print("New color list: ")
for y in lst:
    print(y,end=" ")