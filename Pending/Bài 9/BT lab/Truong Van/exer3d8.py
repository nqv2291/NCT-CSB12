print("program to print n first primes\n")
#create function
def primes(num):
    checknum =1
    if num ==2: #em dung 1 cai num = 2 luôn là vì nếu cho nó xuống cái dưới thì x nó không tồn tại
        checknum = 1
    else:
        for x in range(2,num):
            if num%x==0:
                checknum=0
                break
    return checknum
#input n
n =int(input('input n:  '))
#initialize two var
list1=[]
i=2
#start to count
while len(list1)<n and i>=2:
    var = primes(i)
    if var ==1:
        list1.append(i)
    i+=1
print(list1)

        
