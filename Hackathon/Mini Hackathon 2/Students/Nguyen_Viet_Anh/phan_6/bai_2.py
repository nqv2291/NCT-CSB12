name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT" ]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]
populationDENTI = []


for i in range(len(area)):
    a = population[i] / area[i]
    populationDENTI.append(a)

Sum = sum(populationDENTI)
b = len(name)

average = Sum / b

print(f"Average population density: {average}")
