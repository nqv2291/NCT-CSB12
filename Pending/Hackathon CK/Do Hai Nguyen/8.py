n1=1
n2=0
n=int(input("Input a number: "))
if n==1:
    print("frist fibonacci numbers: 1")
else:
    print("the first",n,"numbers in fibonacci numbers")
    for i in range(0,n):
        print(n1,end=" ")
        nth=n1+n2
        n2=n1
        n1=nth
    