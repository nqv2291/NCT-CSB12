# get input
print('Number of items: ', end='')
num = int(input())
print()

arr = []
for i in range(num):
  print(f'Item {i+1}: ', end='')
  name = input()
  print(f'Price of item {i+1}: ', end='')
  price = float(input())
  print()
  arr.append((name, price))


# find average price
total = 0
for item in arr:
  total += item[1]
average = total / num
print('Average price:', average)

# find items above average price
print('Item(s) above average price: ', end='')
for item in arr:
  if item[1] > average:
    print(item, end=' ')