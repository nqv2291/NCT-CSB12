# initialize dictionaries
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

# get user input
print('Input a brand: ', end='')
brand = input()
print('Input amount to buy: ', end='')
amount = int(input())

# print total price
total_price = prices[brand] * amount
print('Total price:', total_price)

# update dictionary & print
amounts[brand] -= amount
print('Available products:')
for brand, amount in amounts.items():
  print(f'- {brand}: {amount}')