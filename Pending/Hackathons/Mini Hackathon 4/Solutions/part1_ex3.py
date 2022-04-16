# initialize dictionary
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}

# get user input
print('Input a brand: ', end='')
brand = input()

# print result
print(f'Available {brand}s: {amounts[brand]}')