    # Part 2
    # Bài 1
# color= ["green","red","blue","yellow","purple"]
# print(color)
# print(type(color))
# for x in color:
#     print(x, end=" ")

# print("\ncó ",len(color),"loại màu")

# color_position= int(input("color position "))
# if color_position>=1:
#     print("tên màu là", color[color_position-1])
# elif color_position==0:
#     print(" ko có nha")
# else:
#     print("tên màu là", color[color_position])


    # Bài 2
color= ["green","red","blue","yellow","purple"]
print(color)
print(type(color))
for x in color:
    print(x, end=" ")

print("\ncó ",len(color),"loại màu")

color_position= int(input("color position to delete "))

if color_position>=1:
    del color[color_position-1]
    for i in color:
        print(i, end=" ")
elif color_position==0:
    for i in color:
        print(color)
else:
    del color[color_position]
    for i in color:
        print(i, end=" ")

delete_item= input("color to delete")
if delete_item != int:
    slice()
    print(color)
else:
    print("anho")




