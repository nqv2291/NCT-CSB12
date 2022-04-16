# get user inputs
print('Your input: ', end='')
inp = input()

# METHOD 1 - Using built-in string method
print('Capitalized:', inp.upper())

# METHOD 2 - Hand coding
print('Capitalized: ', end='')
distance = ord('A') - ord('a')  # distance between lower & upper characters
for ch in inp:
  if ch > 'a' and ch < 'z':
    print(chr(ord(ch) + distance), end='')
  else:
    print(ch, end='')