# Part 1 :---------------------------------------
#Bài 1:
# def so_chan(n):
#     # flag = 0  # So le
#     # flag = 1 # So chan

#     if n %2 == 0:
#         flag =1 
#         return flag
#     else:
#         flag = 0
#         return flag

# n = int(input("Số bạn muốn :"))

# check = so_chan(n)

# if check == 1:
#     print(n,"là số chẵn")
# else:
#     print(n,"ko pải là số chẵn")

# Bài 2:

# def area_of_circle(n):
#     area = n*3.14
#     return area

# n = float(input("Bán kính: "))

# circle = area_of_circle(n)

# print("Diện tích là: ",circle)

# Bài 3:

# def reverse_string(n):
#     """Return a reversed copy of `s`"""
#     return n[::-1]


# n = str(input("Nhập kí tự string bạn muốn: "))
# string = reverse_string(n)
# print(string)


# Bài 4 :

# def palidrome(n):
#     m = n[::-1]
#     if m != n :
#         flag = 1 # là palidrone
#         return flag
#     else:
#         flag = 0  # ko pải là palidrome
#         return flag


# n = str(input("Nhập chữ bạn muốn: "))

# palidrome_string = palidrome(n)

# if palidrome_string == 1:
#     print(n,"là palidrome ")
# else:
#     print(n,"ko pải là palidrome")


# Part 2:-------------------------------------------

# Bài 1:

# def tinhgiaithua(n):
#     giai_thua = 1
    
#     if (n == 0 or n == 1):
#         return giai_thua
#     else:
        
#         for i in range(2, n + 1):
#             giai_thua = giai_thua * i
#         return giai_thua
 

# n = int(input("Nhập số nguyên dương n = "))

# print("Giai thừa của", n, "là", tinhgiaithua(n))

# Bài 2:-----------------------------------------------

# from math import nextafter


# numbers = [122,21,-11,-90,64,12]

# def sap_xep_tang_dan(numbers):
 
#     lenth = len(numbers)
 
    
#     for i in range(0, lenth - 1):
#         for j in range(i + 1, lenth):
#             if (numbers[i] > numbers[j]):
#                 # Hoán đổi vị trí
#                 tmp = numbers[i]
#                 numbers[i] = numbers[j]
#                 numbers[j] = tmp
 
#     return numbers

# list_num = sap_xep_tang_dan(numbers)

# print("dãy số ban đầu: ",numbers)
# print("dãy số sau sắp xếp: ",list_num)

# Bài 3:----------------------------------------------

# def fibonacci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1
 
#     if (n < 0):
#         return -1
#     elif (n == 0 or n == 1):
#         return n
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn
 
# n = int(input("độ dài bạn muốn:"))
# print("Dãy số của bạn")
# sb = ""


# for i in range(0, n):
#     sb = sb + str(fibonacci(i)) + ", "
# print(sb)

# Part 3:------------------------------------------------


print("welcome to my game")

print(" -P- \n --D \n K-- ")

print("You have 5 choice A, W, S, D and Q")
print("A: Left \nW: Up \nS: Down \nD :Right \nQ: Quit")

Your_choice = str(input("Your move: "))



if Your_choice == "Q":
    print("Bye \nSee you again!")
    if Your_choice == "D":
        print(" --P \n --D \n K-- ")
    elif Your_choice == "S":
        print("Game over")
elif Your_choice == "S":
    print(" --- \n -PD \n K-- ")
    if Your_choice == "D":
        print("Game over")
elif Your_choice == "A":
    print(" P-- \n --D \n K-- ")
    
