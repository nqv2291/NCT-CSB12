import random
from dict import skill_set
from dict import player

for i in range(len(skill_set)):
    print(f"Skill {i+1}: {skill_set[i]['Name']}")

skill=int(input("Chose skill number: "))
print("You chose",skill_set[skill-1]['Name'])
if player["Lv"]>=skill_set[skill-1]['Minimum level']:
  if random.random() <= skill_set[skill-1]['Hit rate']:
      print("Damage: ",skill_set[skill-1]['Damage'])
  else:
      print("You missed")
else:
    print("Cannot deploy. Required lv",skill_set[skill-1]['Minimum level'])