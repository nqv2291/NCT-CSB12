# calculate factorial
def cal_fact(num):
  result = 1
  for i in range(2, num+1):
    result *= i
  return result

# get user input
print('Input a number: ', end='')
num = int(input())

# print result
print(f'{num}! = {cal_fact(num)}')