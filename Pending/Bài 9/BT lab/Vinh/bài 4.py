def giaithua(a):
    tich=1
    for i in range (1,a+1):
        tich=tich*i
    return tich
tong=0
n=int(input("Số bạn muốn nhập là: "))
for i in range (1,n):
    tong=tong+ giaithua(i)
print(f"Tổng giai thừa n số từ 0 đến {n-1} là {tong+1}") #do 0!=1 đây là TH đặc biệt
