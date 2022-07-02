Skill_1 = {'Name': 'Tackle', 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3

}

Skill_2 = {'Name': 'Quick Attack', 'Minimum level': 2, 'Damage': 3, 'Hit rate': 0.5

}
Skill_3 = {'Name': 'Strong Kick', 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2

}

Skills = {
    'Skill 1': Skill_1['Name'],
    'Skill 2': Skill_2['Name'],
    'Skill 3': Skill_3['Name']
}
for key, value in Skills.items():
    print(f"{'  {}'.format(key)}: {value}")