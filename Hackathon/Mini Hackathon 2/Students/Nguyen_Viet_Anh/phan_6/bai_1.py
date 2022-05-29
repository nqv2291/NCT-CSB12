name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT" ]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]
populationDENTI = []

print("Popluation density of: ")

for i in range(len(area)):
    a = population[i] / area[i]
    populationDENTI.append(a)

for a in range(len(area)):
    print("- ",name[a], ": ", populationDENTI[a])
