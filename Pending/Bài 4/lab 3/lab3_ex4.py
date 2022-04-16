# get input
print('Input number: ', end='')
num = int(input())

# check conditions
if (num % 3 == 0) or (num % 5 == 0):  # if divisible by 3 or 5
  if num % 5 != 0:
    print(f'{num} is divisible by 3')
  elif num % 3 != 0:
    print(f'{num} is divisible by 5')
  else:
    print(f'{num} is divisible by 3 and 5')

else:                                 # else: not divisible by 3 or 5
  print(f'{num} is not divisible by 3 or 5')