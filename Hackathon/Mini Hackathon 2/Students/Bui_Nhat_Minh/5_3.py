city_list = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
area_list = [9.224, 43.35, 12.04, 9.96, 10.09]
population_list = [247100, 333300, 266800, 420900, 318000]
print('Names of:')
print(
    f'- Most populated dist.: {city_list[population_list.index(max(population_list))]}')
print(
    f'- Least populated dist.: {city_list[population_list.index(min(population_list))]}')
