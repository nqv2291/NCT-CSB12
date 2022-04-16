list_of_colors = list(("blue", "teal","green"))
print("color list:") 
for color in list_of_colors: 
    print(color, end=', ')
print("")
a=int(input("input position: "))
print("color at position",a,":", list_of_colors[a-1])

b=int(input("color to delete: "))
list_of_colors.pop(a-1)
print("new color list:", end=' ')
for color in list_of_colors:
    print(color, end=', ')
print("")
list_of_colors.remove(input("color to delete: "))
for color in list_of_colors:
    print(color)
