# initialize dictionary
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}

# get user input
print('Input a brand: ', end='')
brand = input()
print('Input amount: ', end='')
amount = int(input())

# add new brand
amounts[brand] = amount

# print result
print('Available products:')
for brand, amount in amounts.items():
  print(f'- {brand}: {amount}')