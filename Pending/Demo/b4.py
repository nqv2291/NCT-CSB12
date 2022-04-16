n = int(input("num of items: "))

menu = []
for i in range(n):
    item = input(f"item {i+1}: ")
    price = float(input(f"Price of item {i+1}: "))
    menu.append((item, price))

print(menu)

sum_price = 0
for i in menu:
    sum_price += i[1]
avg = sum_price/n
print(f"average = {avg}")

for i in menu:
    if i[1] > avg:
        print(i, end= " ")


