str = input('Input sequence: ')
frequency = {}
for letter in str:
    frequency[letter] = frequency.get(letter, 0) + 1
print('Frequency of characters:')
print(frequency)
