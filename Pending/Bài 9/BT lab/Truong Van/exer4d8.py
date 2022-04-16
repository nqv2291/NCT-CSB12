#create function
def fac(num):
    s=1
    for x in range(1,num+1):
        s=s*x
    return s #return fact of num
#input n
n = int(input('input n:  '))
#create two first var
sum=0
a=1
#start cal
for i in range(1,n+1): # get value of i from 1 to n to cal fact
    sum= sum+(fac(i)/a)
    a+=1
print(sum)


    