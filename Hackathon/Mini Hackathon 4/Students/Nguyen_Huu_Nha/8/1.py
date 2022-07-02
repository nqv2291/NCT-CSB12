character = {
'Name': 'Light',
'Age': 17,
'Strength': 8,
'Defense': 10,
'HP': 100,
'Backpack': 'Shield, ''Bread Loaf, ', 
'Gold': 100,
'Level': 2
}
Skill_1 = {'Name': 'Tackle', 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3

}

Skill_2 = {'Name': 'Quick Attack', 'Minimum level': 2, 'Damage': 3, 'Hit rate': 0.5

}
Skill_3 = {'Name': 'Strong Kick', 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2

}

Skills = {
    'Skill 1': {'Name': 'Tackle', 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3},
    'Skill 2': {'Name': 'Quick Attack', 'Minimum level': 2, 'Damage': 3, 'Hit rate': 0.5},
    'Skill 3': {'Name': 'Strong Kick', 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2}
}
Skillss = {
    'Skill 1': 'Tackle',
    'Skill 2': 'Quick Attack',
    'Skill 3': 'Strong Kick'
}
Skill = list(Skills.values())
for key, value in Skillss.items():
    print(f"{'  {}'.format(key)}: {value}")
a = int(input ("Choose skill by number:"))
print (f"You chose {Skill[a-1]['Name']}")
if Skill[a-1]['Minimum level'] <= character['Level']:
    print (f"Damage: {Skill[a-1]['Damage']}")
else: 
    print (f"Cannot deploy, Required level {Skill[a-1]['Minimum level']}")