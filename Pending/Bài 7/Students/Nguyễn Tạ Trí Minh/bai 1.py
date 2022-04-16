color_list = ["red blue green"]


for i in range(len(color_list)):
    print("Color list:" + color_list[i])

addcolor = input("Input a new color: ")
color_list.extend(addcolor)

print(color_list)
