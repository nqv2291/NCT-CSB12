def facto(n): return n*facto(n-1) if n>0 else 1
##Hàm giai thừa đệ quy 1 dòng luôn kk 😎

n = int(input("Nhập vào số nguyên dương: "))
while n<=0:
    n = int(input("Lỗi, nhập lại một số nguyên dương: "))

sum = 0
for i in range(1,n+1):
    placeholder = facto(i)/i
    sum += placeholder

print(sum)