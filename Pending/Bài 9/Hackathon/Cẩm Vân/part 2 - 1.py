n = int(input("Input number: "))
import math 
giai_thua = 1 
if n > 0 : 
  for i in range(1, n + 1):
    giai_thua = giai_thua * i 
  print("Result:", giai_thua)
else :
  print("Nhập lại") 

