def print_fibo(n):
    dem=0
    start1,start2=1,1
    while dem<n and not start1 == "None":
        print(start1)
        term=start1+start2
        start1=start2
        start2=term
        dem += 1
n=int(input("input a number:"))
while n <=0:
    n=int(input("input a postive number :)) :"))
print_fibo(n)