n = int(input("Nhập tháng: "))
if n ==2:
    print("Tháng" ,n, "có 28 hoặc 29 ngày")
elif n == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("Tháng" ,n, "có 31 ngày")
else:
    print("Tháng" ,n, "có 30 ngày")