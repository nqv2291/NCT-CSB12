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
skills = [
    {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3
    }, {
        'Name': 'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5
    }, {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
    },
]
for i in range(len(skills)):
    print(f"-Skill {i+1}: {skills[i]['Name']}")
skill_chosen = int(input('Choose skill by number: '))
print()
print(f"You chose {skills[skill_chosen - 1]['Name']}.")
if (skills[skill_chosen - 1]['Minimum level'] <= character['Level']):
    print(f"Damage: {skills[skill_chosen - 1]['Damage']}")
else:
    print(
        f"Cannot deploy. Required level {skills[skill_chosen - 1]['Minimum level']}.")
