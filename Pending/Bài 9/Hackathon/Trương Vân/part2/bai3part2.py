#funtion to print n fibo num
def print_fibo(n):
    list_num =[0,1]
    if n==0:
        print("list is []")
    elif n==1:
        print("list is [0]")
    elif n==2:
        print("list is [0,1]")
    else:
        for i in range(n):
            while len(list_num)<n:
                list_num.append(list_num[i-1]+list_num[i-2])
        print(list_num)

n = input("input n fibo numbers :  ")
n=int(n)
print_fibo(n)
