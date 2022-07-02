# 1.1 init character dictionary
character = {'name': 'Light',
            'Age': 17,
            'Strength': 8,
            'Defense': 10,
            'HP': 100,
            'Backpack': ['Shield', 'Bread Loaf'],
            'Gold': 100,
            'Level': 2
            }
print(character)

# 1.2 Update characer dictionary (1)
character['Gold'] += 50
print(character)

# 1.3 Update characer dictionary (2)
character['Backpack'].append('Fint Stone')
print(character)

# 1.4 Update characer dictionary (3)
character['Pocket'] = ['MonsterDex', 'Flashlight']
print(character)