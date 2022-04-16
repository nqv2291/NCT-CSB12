num=[-1,2,15,20,4]
sum=0
number=int(input("Tìm số: "))
if num.count(number) == True:
    print("Number found at position",num.index(number)+1)
else:
    print("Number not found ")
for i in range(0,len(num)):
    sum=sum + num[i]
print("Tổng:",sum)
print("Tạo danh sách số")
print("Bấm 0 để dừng")
while True:
    new=int(input("Thêm số: "))
    if new == 0:
        break
    else:
        num.append(new)
for i in range(0,len(num)):
    sum=sum + num[i]
print("Tổng:",sum-80)
