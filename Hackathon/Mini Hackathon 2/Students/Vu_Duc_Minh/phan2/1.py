lst = ["blue", "red", "teal", "green"]
print("Color list:", ', '.join(lst))
a = int(input("Please input a number: "))
while a > int(len(lst)):
    a = int(input("Please input a number that's smaller than", len(lst),":"))
print("Color at position",a,":",lst[a-1])