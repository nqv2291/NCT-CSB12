lst = []
check = "y"
print("== Welcome to MindX Restaurant ==")

while check == "y":
    a = input("Please choose a dish: ")
    count = lst.count(a)
    if count > 0:
        print("You chose this already.", end = ' ')
    else:
        print("Great choice!", end = ' ')
        lst.append(a)
    check = input("Anything else? (y/n): ")

print("Well done! Your order: ")
for i in lst:
    print("-", i)
    
