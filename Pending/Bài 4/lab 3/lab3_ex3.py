# get input
print('Input character: ', end='')
ch = input()

# check conditions
if ch >= '0' and ch <= '9':
  print(f"'{ch}' is a digit")
else:
  print(f"'{ch}' is not a digit")