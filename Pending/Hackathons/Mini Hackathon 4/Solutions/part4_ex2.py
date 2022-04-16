# initialize dictionary
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

# get user input
print('Input a brand: ', end='')
brand = input()
print('Input amount to buy: ', end='')
amount = int(input())

# print result
total_price = prices[brand] * amount
print('Total price:', total_price)