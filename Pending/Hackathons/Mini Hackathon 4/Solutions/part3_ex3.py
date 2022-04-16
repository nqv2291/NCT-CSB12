# initialize dictionary
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

# get user input
print('Input a brand: ', end='')
brand = input()

# print result
print(f'Price of {brand}: {prices[brand]}')