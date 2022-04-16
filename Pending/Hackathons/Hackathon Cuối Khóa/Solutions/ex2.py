# get user input
print('Input a: ', end='')
a = float(input())  # assume a != 0
print('Input b: ', end='')
b = float(input())
print('Input c: ', end='')
c = float(input())

# calculate solutions
delta = b**2 - 4*a*c  # calculate delta
if delta < 0:    # delta < 0 => no solution
  print('The equation has no solution.')
elif delta > 0:  # delta > 0 => 2 solutions
  print('The equation has 2 solutions.')
  x1 = (-b + delta**(1/2)) / (2*a)
  x2 = (-b - delta**(1/2)) / (2*a)
  print(f'x = {x1}   or   x = {x2}')
else:            # delta == 0 => 1 solution
  print('The equation has 1 solution.')
  x = -b / (2*a)
  print(f'x = {x}')