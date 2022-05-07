from turtle import *

# get input
print('Input length 1: ', end='')
len1 = float(input())
print('Input length 2: ', end='')
len2 = float(input())
print('Input length 3: ', end='')
len3 = float(input())

# if 3 segments can form a triangle
if (len1 < len2 + len3) and (len2 < len1 + len3) and (len3 < len1 + len2):

  # check for equilateral triangle
  if len1 == len2 and len2 == len3:
    print('The 3 line segments can form an equilateral triangle.')
    # draw the triangle
    shape('turtle')
    forward(len1)
    left(120)
    forward(len1)
    left(120)
    forward(len1)
    mainloop()

  # check for right triangle using Pythagorean Theorem
  elif (len1**2 == len2**2 + len3**2) or (len2**2 == len1**2 + len3**2) or (len3**2 == len1**2 + len2**2):
    print('The 3 line segments can form a right triangle.')

  # else: just a normal triangle
  else:
    print('The 3 line segments can form a triangle.')

else:  # 3 segments cannot form a triangle
  print('The 3 line segments cannot form a triangle.')