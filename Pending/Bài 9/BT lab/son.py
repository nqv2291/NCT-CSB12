# Bài 1:-----------------------------------

# import math
# def is_int(n):
#     #flag = 1 => số nguyên
#     #flag = 0 => số thực

#     flag = 1
#     if (math.ceil(n) != math.floor(n)):
#         flag = 0
#     return flag


# n = float(input("nhap mot so: "))


# check = is_int(n)
 
# if check == 1:
#     print(n," la so nguyen")
# else:
#     print(n," la so thuc")

# Bài 2:-------------------------------------------



def is_prime(n):
    #flag = 0 => ko phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1
    if (n <2):    #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
        flag = 0
        return flag 
    
    
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break #Chỉ thấy 1 ước số là đủ và break vòng lặp
    return flag

n = int(input(" nhap so tu nhien: "))


num = is_prime(n)

if num == 1:
    print(n,"is a prime")
else:
    print(n,"is not a prime")

# Bài 3:

# def is_prime(n):
#     #flag = 0 => ko phải số nguyên tố
#     #flag = 1 => số nguyên tố
#     flag = 1
#     if (n <2):    #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
#         flag = 0
#         return flag 
    
    
#     for p in range(2, n):
#         if n % p == 0:
#             flag = 0
#             break #Chỉ thấy 1 ước số là đủ và break vòng lặp
#     return flag


# n = int(input("Nhập số bạn muốn: "))

# for i in range(n):
#     num = is_prime(i)
#     if num == 1 :
#         print(i)

# Bài 4: e chịu

# Bài 5:--------------------------------------------------

# from datetime import datetime

# now = datetime.now()


# date_time = now.strftime("%Y/%m/%d")
# print("Today is ",date_time)

# time_now = now.strftime("%H:%M:%S")
# print("Time right now is ",time_now)


    
