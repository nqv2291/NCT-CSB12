# initialize dictionary
phones = {'Iphone12': 28000000, 'Samsung N10': 16000000,
          'Oppo 93': 7500000, 'Vsmart': 7400000, 'Vivo': 4200000}

# get user inputs
print('Input your budget: ', end='')
budget = int(input())

# print result
print('Phones that fit your budget:')
found = False  # flag variable. turns True if found at least 1 phone
for name, price in phones.items():
  if price <= budget:
    found = True
    print(f'- {name}: {phones[name]}')

if not found:  # no phone found that match the budget
  print('Not found. Maybe raise the budget a little bit?')