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