# initialize dictionary
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}

# calculate amount of products
s = 0
for amount in amounts.values():
  s += amount

# print result
print('Total products:', s)