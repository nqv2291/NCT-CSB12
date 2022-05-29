# get input
print('Input a positive number: ', end='')
num = int(input())

# generate the fibonacci list
print(f'First {num} Fibonacci number(s): ', end='')

# METHOD 1: Using list to store the whole sequence
fibo = [1, 1]  # initialize first 2 elements
for i in range(num):
  if i >= 2:
    fibo.append(fibo[i-1] + fibo[i-2])  # find the next number
  print(fibo[i], end=' ')


# METHOD 2: Using list to store only the last 2 numbers
# fibo = [1, 0]
# for i in range(num):
#   print(fibo[i % 2], end=' ')
#   fibo[(i+1) % 2] += fibo[i % 2]  # find the next number

# explain: if i is even, fibo[0] is bigger | if i is odd, fibo[1] is bigger