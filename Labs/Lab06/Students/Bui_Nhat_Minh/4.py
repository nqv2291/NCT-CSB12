n = int(input('Number of items: '))
print()

item_list = []
for i in range(n):
    item = input(f'Item {i+1}: ')
    price = float(input(f'Price of item {i+1}: '))
    item_list.append([item, price])
    print()

total_price = 0
for i in range(len(item_list)):
    total_price += item_list[i][1]
mean_price = total_price / len(item_list)
print(f'Average price: {mean_price}')

print('Item(s) about average price:', end=' ')
for i in range(len(item_list)):
    if item_list[i][1] > mean_price:
        print(f"('{item_list[i][0]}', {item_list[i][1]})", end=' ')
