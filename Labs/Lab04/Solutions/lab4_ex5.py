print('Numbers with sum of digits = 9:')

# initialize count and num
count = 0
num = 1000

# repeat while count not reached 10
while count < 10:

  # calculate sum of digits
  sum = 0
  num2 = num
  while num2 > 0:
    sum += num2 % 10
    num2 //= 10

  # if sum of digits equals 9
  if sum == 9:
    count += 1  # increase count
    print(num, end=' ')  # print number

  # increase number for next searching step
  num += 1