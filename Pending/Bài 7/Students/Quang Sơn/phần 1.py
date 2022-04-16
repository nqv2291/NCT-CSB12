#bài 1:
list_of_colors = list(('blue', 'teal','green'))
#bài 2:
print("color list:") 
for item in list_of_colors: 
    print(item, end=', ')
#bài 3
print("")
list_of_colors.append(input("input a new color: "))
print("new color list:")
for item in list_of_colors:
    print(item, end=', ')


