arr_encoded = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
               'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

# initialize empty result string
str_decoded = ''

# traverse backward the encoded list
for i in range(len(arr_encoded)-1, -1, -1):
  str_decoded += arr_encoded[i]

print(str_decoded)