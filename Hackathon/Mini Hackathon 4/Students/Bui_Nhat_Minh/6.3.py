character = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}
character['Backpack'].append('FlintStone')
result = 'Backpack: '
for item in character['Backpack']:
    result += item + ', '
print(result[:-2])
