# check if a number is even
def is_even(num):
  return num % 2 == 0

# get user input
print('Input a number: ', end='')
num = int(input())

# print result
if is_even(num):
  print('This number is even')
else:
  print('This number is not even')