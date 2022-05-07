# get input
print('Input number: ', end='')
num = float(input())

# check conditions
if num == int(num):
  print(f'{int(num)} is an integer')
else:
  print(f'{num} is not an integer')