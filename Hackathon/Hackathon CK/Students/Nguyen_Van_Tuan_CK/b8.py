print('Input a natural number: ', end='')
num = int(input())
print(f'First {num} Fibonacci number(s): ', end='')
fibonacci = [1, 1]  
for i in range(num):
  if i >= 2:
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])  
  print(fibonacci[i], end=' ')