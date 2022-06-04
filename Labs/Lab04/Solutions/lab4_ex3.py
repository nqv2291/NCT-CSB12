# get input
print('Input number: ', end='')
num = int(input())

# check invalid case
if num < 0:
  print('Invalid')
else:  # if not invalid, calculate factorial
  fact = 1
  for i in range(2, num+1):
    fact *= i
  print(f'{num}! = {fact}')