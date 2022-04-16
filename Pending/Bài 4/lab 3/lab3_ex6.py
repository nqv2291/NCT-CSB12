# get input
print('Input length 1: ', end='')
len1 = float(input())
print('Input length 2: ', end='')
len2 = float(input())
print('Input length 3: ', end='')
len3 = float(input())

# check conditions
if (len1 < len2 + len3) and (len2 < len1 + len3) and (len3 < len1 + len2):
  print('The 3 line segments can form a triangle.')
else:
  print('The 3 line segments cannot form a triangle.')