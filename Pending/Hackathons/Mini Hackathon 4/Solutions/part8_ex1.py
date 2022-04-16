# initialize data
char = {'Name': 'Light', 'Age': 17, 'Strength': 8, 'Defense': 10, 'HP': 100,
        'Backpack': ['Shield', 'Bread Loaf'], 'Gold': 100, 'Level': 2}
skills = [
  {'Name': 'Tackle', 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3},
  {'Name': 'Quick Attack', 'Minimum level': 2, 'Damage': 3, 'Hit rate': 0.5},
  {'Name': 'Strong Kick', 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2}
]

# print list of skills
for i, skill in enumerate(skills):
  print(f'Skill {i+1}: {skill["Name"]}')

# get user input
print('Choose skill by number: ', end='')
choice = int(input())

# print result
for i, skill in enumerate(skills):
  if i+1 == choice:  # find the skill by index
    print(f'\nYou chose {skill["Name"]}.')
    if char['Level'] >= skill['Minimum level']:  # valid skill
      print(f'Damage: {skill["Damage"]}')
    else:                                        # invalid skill
      print(f'Cannot deploy. Required level {skill["Minimum level"]}')