# print n first numbers in Fibonacci sequence
def print_fibo(num):
  
  if num == 1:  # special case
    print(f'First Fibonacci number: 1')
    return

  # generate the Fibo sequence
  fibo = [1, 1]
  for i in range(num-2):
    fibo.append(fibo[-1] + fibo[-2])

  # print the sequence
  print(f'First {num} Fibonacci numbers: ', end='')
  for el in fibo:
    print(el, end=' ')


# get user input
print('Input a number: ', end='')
num = int(input())

# print result
print_fibo(num)