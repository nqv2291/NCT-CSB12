# 2.1 init skill list
skills = {
    'skill 1':{
        'name': 'tackle',
        'minimum level': 1,
        'damage': 5,
        'hit rate': 0.3
        },
    'skill 2':{
        'name': 'quick attack',
        'minimum level': 2,
        'damage': 3,
        'hit rate': 0.5
        },
    'skill 3':{
        'name': 'strong kick',
        'minimum level': 4,
        'damage': 9,
        'hit rate': 0.2
        }
    }

# 2.2 Print skill list (1)
print("\nEx 2.2:")
for i, skill in enumerate(skills.keys()):
    skill_name = skills[skill]['name']
    print(str(i + 1) + ". " + skill_name.title())

# 2.3 Print skill list (2)
print("\nEx 2.3:")
for skill in skills.keys():
    print(skill.title() + ":")
    for info, detail in skills[skill].items():
        print('\t' + info.title() + ": " + str(detail).title())