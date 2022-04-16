num = float(input("Input number: "))
def is_num(num):
  if num.is_integer() :
   print(f'{int(num)} is an integer')
  else:
   print(f'{num} is not an integer')
is_num(num)
