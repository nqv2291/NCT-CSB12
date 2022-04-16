    # Part 1
color1 = ["blue"]
color2 = ["green"]
color3 = ["red"]
color=color1+color2+color3
for x in color:
    print(x, end=" ")

new= input("\nnew color ")

color.append(new)
for x in color:
    print(x, end=" ")
print("\n",color)

