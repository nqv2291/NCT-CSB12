# get input
print('Input number: ', end='')
num = int(input())

# calculate sum of digits
sum = 0
num2 = num
while num2 > 0:
  sum += num2 % 10
  num2 //= 10

print(f'Sum of digits of {num} = {sum}')