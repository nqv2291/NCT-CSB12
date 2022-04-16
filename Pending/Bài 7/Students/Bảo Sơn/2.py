color=["blue","red","green"]
read=int(input("Input position: "))
print(color[read-1])
dell= input("item to delate: ")
if dell.isdigit() == True:
    dell=int(dell)
    del(color[dell-1])
else:
    color.remove(dell)
print("new color list: ")