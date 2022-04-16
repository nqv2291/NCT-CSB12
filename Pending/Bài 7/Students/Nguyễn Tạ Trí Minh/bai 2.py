Color_list = ["blue, teal, green"]
for i in range(len(Color_list)):
    print("Color list: " + Color_list[i])

position = input("Input position: " + Color_list.pop())


print("Color at position: " + position + f"{Color_list}")
