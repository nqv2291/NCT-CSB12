print("== Welcome to MindX Restaurant ==\n")

food_menu = []
while True:
    food = input('Please choose a dish: ')
    if food in food_menu:
        if input("You chose this already. Anything else? (y/n): ").strip() != "y":
            print()
            break
        print()
    else:
        food_menu.append(food)
        if input("Great choice! Anything else? (y/n): ").strip() != "y":
            print()
            break
        print()

print("Well done! Your order:")
for food in food_menu:
    print(f"- {food}")