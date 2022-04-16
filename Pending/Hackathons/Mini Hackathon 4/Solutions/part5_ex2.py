# initialize dictionaries
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

# calculate total prices
s = 0
for brand in amounts:
  s += amounts[brand] * prices[brand]

# print result
print('Total value of available items:', s)
