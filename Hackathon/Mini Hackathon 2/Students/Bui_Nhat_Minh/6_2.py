city_list = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
area_list = [9.224, 43.35, 12.04, 9.96, 10.09]
population_list = [247100, 333300, 266800, 420900, 318000]
density_list = []
for i in range(len(city_list)):
    density_list.append(population_list[i] / area_list[i])
print(f'Average population density:\n{sum(density_list) / len(density_list)}')
