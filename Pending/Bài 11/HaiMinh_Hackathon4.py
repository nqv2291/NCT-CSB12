# import random
# #Cau 1
# #1
# dictcau1 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }
# print(dictcau1)
# #2
# dictcau1 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# print("Available MACBOOKs:", dictcau1["MACBOOK"])
# #3
# dictcau1 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }
# x = input("Input a brand:")
# print("Available Computers:", dictcau1[x])

# #Cau 2
# #1
# dictcau2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# dictcau2["TOSHIBA"] = 10
# print("Available conducts:", dictcau2)

# #2
# dictcau2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# x = input("Input a brand:")
# y = input("Input amount:")

# dictcau2[x] = y
# print("Available conducts:", dictcau2)

# #3
# dictcau2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# dictcau2["DELL"] = 60
# dictcau2["MACBOOK"] = 2
# print("Available conducts:", dictcau2)

# #4
# dictcau2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# print(dictcau2["HP"] + dictcau2 ["DELL"] + dictcau2["MACBOOK"] + dictcau2["ASUS"])

# #Cau 3
# # 1
# dictcau3 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# print(dictcau3)

# #2
# dictcau3 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# print(("Price of ASUS:"), dictcau3["ASUS"])

# #3
# dictcau3 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# x = input("Input a brand:")

# print("Price of the computer:", dictcau3[x])

# #Cau 4:
# #1
# dictcau4 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }


# print("Total price:", dictcau4["ASUS"]*5)

# #2
# dictcau4 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# x = input("Input a brand:")
# y = int(input("Input amount to buy:"))

# print("Total price:", dictcau4[x]*y)

# #3
# dictcau4 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# dictcau4_2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# x = input("Input a brand:")
# y = int(input("Input amount to buy:"))

# print("Total price:", dictcau4[x]*y)

# dictcau4_2[x] = dictcau4_2[x] - y
# print(dictcau4_2)

# #Cau 5:
# #1
# dictcau5 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# dictcau5_2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# dictcau5_2["HP"] = dictcau5_2["HP"] * dictcau5["HP"]
# dictcau5_2["DELL"] = dictcau5_2["DELL"] * dictcau5["DELL"]
# dictcau5_2["MACBOOK"] = dictcau5_2["MACBOOK"] * dictcau5["MACBOOK"]
# dictcau5_2["ASUS"] = dictcau5_2["ASUS"] * dictcau5["ASUS"]

# print("Total value of available brands", dictcau5_2)

# #2
# dictcau5 = {
#   "HP": 600,
#   "DELL": 650,
#   "MACBOOK": 1200,
#   "ASUS": 400
# }

# dictcau5_2 = {
#   "HP": 20,
#   "DELL": 50,
#   "MACBOOK": 12,
#   "ASUS": 30
# }

# dictcau5_2["HP"] = dictcau5_2["HP"] * dictcau5["HP"]
# dictcau5_2["DELL"] = dictcau5_2["DELL"] * dictcau5["DELL"]
# dictcau5_2["MACBOOK"] = dictcau5_2["MACBOOK"] * dictcau5["MACBOOK"]
# dictcau5_2["ASUS"] = dictcau5_2["ASUS"] * dictcau5["ASUS"]

# print("Total value of available items:", dictcau5_2["HP"] + dictcau5_2["DELL"] + dictcau5_2["MACBOOK"] + dictcau5_2["ASUS"])

# #Cau 6
# #1
# cau6character = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2,
# }
# print(cau6character)

# #2
# cau6character = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2,
# }

# cau6character["Gold"] = cau6character["Gold"] + 50
# print("Gold:", cau6character["Gold"])

# #3
# cau6character = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2,
# }

# cau6character["Backpack"].append("Flintstone")
# print("Backpack:", cau6character["Backpack"])

# #Cau 7
# Cau7characterskill1 = {
#     "Name": "Tackle",
#     "Minimum level": 1,
#     "Damage": 5,
#     "Hit rate": 0.3
# }

# Cau7characterskill2 = {
#     "Name": "Quick Attack",
#     "Minimum level": 2,
#     "Damage": 3,
#     "Hit rate": 0.5
# }

# Cau7characterskill3 = {
#     "Name": "Strong kick",
#     "Minimum level": 4,
#     "Damage": 9,
#     "Hit rate": 0.2
# }

# #2
# Cau7characterskill1 = {
#     "Name": "Tackle",
#     "Minimum level": 1,
#     "Damage": 5,
#     "Hit rate": 0.3
# }

# Cau7characterskill2 = {
#     "Name": "Quick Attack",
#     "Minimum level": 2,
#     "Damage": 3,
#     "Hit rate": 0.5
# }

# Cau7characterskill3 = {
#     "Name": "Strong kick",
#     "Minimum level": 4,
#     "Damage": 9,
#     "Hit rate": 0.2
# }

# print("Skill 1:", Cau7characterskill1["Name"])
# print("Skill 2:", Cau7characterskill2["Name"])
# print("Skill 3:", Cau7characterskill3["Name"])

# #Cau 8
# #1
# Level = 3
# Cau8characterskill1 = {
#     "Name": "Tackle",
#     "Minimum level": 1,
#     "Damage": 5,
#     "Hit rate": 0.3
# }

# Cau8characterskill2 = {
#     "Name": "Quick Attack",
#     "Minimum level": 2,
#     "Damage": 3,
#     "Hit rate": 0.5
# }

# Cau8characterskill3 = {
#     "Name": "Strong kick",
#     "Minimum level": 4,
#     "Damage": 9,
#     "Hit rate": 0.2
# }

# print("Skill 1:", Cau8characterskill1["Name"])
# print("Skill 2:", Cau8characterskill2["Name"])
# print("Skill 3:", Cau8characterskill3["Name"])

# x = int(input("Choose skill by number:"))

# if x == 1:
#     print("You choose", Cau8characterskill1["Name"])
#     if Level >= Cau8characterskill1["Minimum level"]:
#         print("Damage:", Cau8characterskill1["Damage"])
#     else:
#         print("Cannot deploy. Required level 1.")

# if x == 2:
#     print("You choose", Cau8characterskill2["Name"])
#     if Level >= Cau8characterskill2["Minimum level"]:
#         print("Damage:", Cau8characterskill2["Damage"])
#     else:
#         print("Cannot deploy. Required level 2.")

# if x == 3:
#     print("You choose", Cau8characterskill3["Name"])
#     if Level >= Cau8characterskill3["Minimum level"]:
#         print("Damage:", Cau8characterskill3["Damage"])
#     else:
#         print("Cannot deploy. Required level 4.")

# else:
#     print("Skill is not exist")

# #2
# Level = 3
# Cau8characterskill1 = {
#     "Name": "Tackle",
#     "Minimum level": 1,
#     "Damage": 5,
#     "Hit rate": 0.3
# }

# Cau8characterskill2 = {
#     "Name": "Quick Attack",
#     "Minimum level": 2,
#     "Damage": 3,
#     "Hit rate": 0.5
# }

# Cau8characterskill3 = {
#     "Name": "Strong kick",
#     "Minimum level": 4,
#     "Damage": 9,
#     "Hit rate": 0.2
# }

# print("Skill 1:", Cau8characterskill1["Name"])
# print("Skill 2:", Cau8characterskill2["Name"])
# print("Skill 3:", Cau8characterskill3["Name"])

# x = int(input("Choose skill by number:"))

# if x == 1:
#     print("You choose", Cau8characterskill1["Name"])
#     if Level >= Cau8characterskill1["Minimum level"]:
#         if random.random() < Cau8characterskill1["Hit rate"]:
#             print("Damage:", Cau8characterskill1["Damage"])
#         else:
#             print("Missed")
#     else:
#         print("Cannot deploy. Required level 1.")

# if x == 2:
#     print("You choose", Cau8characterskill2["Name"])
#     if Level >= Cau8characterskill2["Minimum level"]:
#         if random.random() < Cau8characterskill2["Hit rate"]:
#             print("Damage:", Cau8characterskill2["Damage"])
#         else:
#             print("Missed")
#     else:
#         print("Cannot deploy. Required level 2.")

# if x == 3:
#     print("You choose", Cau8characterskill3["Name"])
#     if Level >= Cau8characterskill1["Minimum level"]:
#         if random.random() < Cau8characterskill3["Hit rate"]:
#             print("Damage:", Cau8characterskill3["Damage"])
#         else:
#             print("Missed")
#     else:
#         print("Cannot deploy. Required level 4.")

# else:
#     print("Skill is not exist")