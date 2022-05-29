city_list = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
area_list = [9.224, 43.35, 12.04, 9.96, 10.09]
population_list = [247100, 333300, 266800, 420900, 318000]
print('Population density of:')
for i in range(len(city_list)):
    print(f'- {city_list[i]}: {population_list[i] / area_list[i]}')
