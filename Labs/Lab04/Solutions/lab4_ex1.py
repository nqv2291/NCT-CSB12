# get input
print('Input number: ', end='')
num = int(input())

# print staircase

# METHOD 1
line = '#'
for i in range(num):
  print(line)
  line += '#'

# METHOD 2
# print()
# for i in range(num):
#   for j in range(i+1):
#     print('#', end='')
#   print()