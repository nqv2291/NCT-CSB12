from random import random

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

# print player's level
player_level = 2
print(f"Level: {player_level}")

# print all skills
print("Skills list:")
skill_list = list(skills.keys())
for i, skill in enumerate(skill_list):
    skill_name = skills[skill]['name']
    print(str(i + 1) + ". " + skill_name.title())

# get input
user_i = int(input("Choose a skill: "))

# compare user's choice with required level
required_level = skills[skill_list[user_i - 1]]['minimum level']

# # 2.1 Skill level check
# if player_level < required_level:
#     print('This skill requires a higher level!')
# else:    
#     skill_dmg = skills[skill_list[user_i - 1]]['damage']
#     print('=> Damage:',skill_dmg)

# # 2.2 Hit rate
# if player_level < required_level:
#     print('This skill requires a higher level!')
# else:    
#     # random a hit rate in (0, 1)
#     temp_hit_rate = random()

#     # compare randomly generated hit rate with chosen skill hit rate
#     skill_hit_rate = skills[skill_list[user_i - 1]]['hit rate']
#     if temp_hit_rate < skill_hit_rate:
#         skill_dmg = skills[skill_list[user_i - 1]]['damage']
#         print('=> Damage:',skill_dmg)
#     else:
#         print("oops skill missed!")