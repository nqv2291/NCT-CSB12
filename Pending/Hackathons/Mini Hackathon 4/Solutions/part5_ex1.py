# initialize dictionaries
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

# calculate total prices
print('Total value of available brands:')
for brand in amounts:
  print(f'- {brand}: {amounts[brand] * prices[brand]}')