from secrets import choice
from unittest import skip


order=[]

while True:
    dish=input("pls chose a dish: ")

    if (dish in order) == False:
        order.append(dish)
        choices=input("Great choice! Anything else? (y/n): ").lower()
    else:
        print("You alredy ordered this.")
        choices=input("You have alredy odered this! Anything else? (y/n): ").lower()
    if choices=="y":
        continue
    else:
        break

for i in order:
    print(f"- {i} ")