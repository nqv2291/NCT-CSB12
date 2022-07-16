list_food = []

while True:
    a = input("Please choose a dish:")
    if a in list_food:
        b = input ("You chose this already. Anything else? (y/n):")
        if b == 'y':
            print (end='\n')
            continue
        else:
            break
    else:
        list_food.append(a)
        c = input("Great choice! Anything else? (y/n):")
        if c == 'y':
            print (end='\n')
            continue
        else:
            break
print ("Well done! Your order:")
for food in list_food:
    print(f"-{food}")