
num = int(input("Input a number: "))
s = 0
for i in range(s,num):
    print(i)




x = int(input("Please enter the base number: "))
n = int(input("Please enter the number of terms: "))
s = 0
factorial = 1
for j in range(1,n+1):
    factorial = factorial*j
    for i in range(x,n+1):
        s = (x**i)/factorial
        print(s,end='+')
