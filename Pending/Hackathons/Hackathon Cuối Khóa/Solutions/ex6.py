# get user input
print('Input a number: ', end='')
num = int(input())

# calculate number of digits
count = 0
while num > 0:
  count += 1
  num //= 10

# print result
print(f'This number has {count} digit(s).')