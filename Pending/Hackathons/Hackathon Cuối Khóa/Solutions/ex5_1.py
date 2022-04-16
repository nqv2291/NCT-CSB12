# initialize dictionary
phones = {'Iphone12': 28000000, 'Samsung N10': 16000000,
          'Oppo 93': 7500000, 'Vsmart': 7400000, 'Vivo': 4200000}

# get user inputs
print("Input name of a phone: ", end='')
name = input()

# print result
print(f'Price of {name}: {phones[name]}')