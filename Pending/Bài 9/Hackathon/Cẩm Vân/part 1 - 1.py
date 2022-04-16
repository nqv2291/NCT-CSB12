def check_odd_even(n):
    #flag = 1 => số lẻ  ;   flag = 0 => số chẵn
    flag = 1
    if( n % 2 == 0):
        flag= 0
    return flag 

n = int(input("Enter a number: "))

check = check_odd_even(n)
if check == 1:
    print(n,"là số lẻ")
else:
    print(n,"là số chẵn")