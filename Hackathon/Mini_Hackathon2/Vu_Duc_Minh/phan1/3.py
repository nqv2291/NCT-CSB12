lst = ["blue", "red", "teal", "green"]
print("Current color list:", ', '.join(lst))

# add the inputed color to list
b = input("Input a color: ")
lst.append(b)
print("New color list: ", ', '.join(lst))