# get input
n = int(input("Number of items: "))

menu = []
total = 0
for i in range(n):
    name = input(f"\nItem {i+1}: ")
    price = float(input(f"Price of item {i+1}: "))
    # add new item to menu
    menu.append((name, price))
    # add new item price to total price
    total = total + price

# find average price
avg_price = total/n
print(f"\nAverage price: {avg_price}")

# find items above average price
print(f"Item(s) above average price:", end=" ")
for item in menu:
    if item[1] > avg_price:
        print(item, end=" ")