# initialize dictionary
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}

# update dictionary
amounts['DELL'] = 60
amounts['MACBOOK'] = 2

# print result
print('Available products:')
for brand, amount in amounts.items():
  print(f'- {brand}: {amount}')