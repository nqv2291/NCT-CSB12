# calculate circle's area from radius
def cal_area(radius):
  return 3.14*radius**2

# get user input
print('Input radius: ', end='')
radius = float(input())

# print result
print("Circle's radius", cal_area(radius))