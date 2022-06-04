name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT" ]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]
population_density = []

for i in range(len(area)):
    a = population[i] / area[i]
    population_density.append(a)
print("Population density of: ")
for i in range(len(name)):
    print(f"- {name[i]}: {population_density[i]}")

print(f'Average population density:\n{sum(population_density) / len(population_density)}')