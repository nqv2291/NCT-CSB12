print('Date in MM/DD/YYYY format: ', end='')
date = input()

month = date[:2]
day = date[3:5]
year = date[-4:]
print(f'Date in DD/MM/YYYY format: {day}/{month}/{year}')