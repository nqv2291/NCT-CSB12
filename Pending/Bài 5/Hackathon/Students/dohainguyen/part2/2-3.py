x=int(input("input number :"))
if x%2==0:
   for i in range(1,x,2):
        print(i)
else:
    for i in range(1,x+1,2):
        print(i)