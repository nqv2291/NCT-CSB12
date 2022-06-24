number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
number = {}
for key, value in enumerate(number_list):
    number[value] = key + 1
roman_input = input('Input a Roman number: ')
try:
    print(number[roman_input])
except:
    print('Not found.')
