import math
num = int(input("enter your number"))
def sumdivi(num):
    facti = math.factorial(num)
    print(f"{num}! is {facti}")
    
sumdivi(num)

num_list = [ 1 , 3 , 5 , 8 , 2 , 4 , 6 , 0]
def sort_list(num_list):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):

            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]

    print(num_list)
sort_list(num_list)

fibolist = [1]

endd = int(input("enter a number"))
def list_fibo(endd):
    fi_num = 0
    fi_num_con = 1
    for i in range(0 , endd):
        sum = fi_num + fi_num_con
        fibolist.append(sum)
        fi_num = fi_num_con
        fi_num_con = sum

    print(f"your fibonacci list: {fibolist}")
list_fibo(endd)
