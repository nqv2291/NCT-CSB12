# initialize dictionary
char = {'Name': 'Light', 'Age': 17, 'Strength': 8, 'Defense': 10, 'HP': 100,
        'Backpack': ['Shield', 'Bread Loaf'], 'Gold': 100, 'Level': 2}

# update char
char['Backpack'].append('FlintStone')

# print result
print('Backpack: ', end='')
for item in char['Backpack'][:-1]:
  print(item, end=', ')
print(char['Backpack'][-1])