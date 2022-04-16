fibonacy = [1, 1]

n = int(input("n = "))

fibo = [1, 0]
for i in range(n):
  print(fibo[i % 2], end=' ')
  fibo[(i+1) % 2] += fibo[i % 2]  # find the next number
