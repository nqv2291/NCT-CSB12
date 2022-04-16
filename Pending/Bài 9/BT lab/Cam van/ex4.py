n = int(input("Input number: "))
import math 
giai_thua = 1 
tong = 0 
for i in range(1, n + 1):
    giai_thua = giai_thua * i 
    tong = tong + giai_thua / i
print("Result: ", tong)