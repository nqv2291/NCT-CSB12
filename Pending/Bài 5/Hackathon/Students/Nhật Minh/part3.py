    # Bai 1
# num= float(input(" so sanh voi 10 "))
# if num<10:
#     print(num, "be hon 10")
# elif num==10:
#     print(num, "= 10")
# else:
#     print(num, "lon hon 10")

    # Bai 2
# num= float(input(" so chan hay le"))
# if num%2==0:
#     print(num, "so chan")
# else:
#     print(num, "so le")

    # Bai 3
month= int(input(" thang nao do "))
year= int(input(" nam nao do "))
if month>12 or month<=0:
    print("biet so thang trong 1 nam khong vay ")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month ==10 or month ==12:
    print("co 31 ngay")
elif month==2:
    if year%4==0 and year%100!=0 or year%400==0:
        print(" co 29 ngay")
    else:
        print(" co 28 ngay")
else:
    print("co 30 ngay")