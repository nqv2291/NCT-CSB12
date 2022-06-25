
player = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense':10,
    'HP': 100,
    'Backpack': 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2,
}

player ['Gold'] += 50
for key, value in player.items(): 
    print("-", key + ":", value)