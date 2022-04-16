list_of_colors = list(('blue', 'teal','green'))
print("color list:") 
for item in list_of_colors: 
    print(item, end=', ')
list_of_colors.append(input("input a new color: "))
print("new color list:")
for item in list_of_colors:
    print(item, end=', ') 