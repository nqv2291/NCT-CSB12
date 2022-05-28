nT = int(input("Input a positive number: "))
n1 = 0
n2 = 1
count = 0
if nT <= 0:
   print("Please enter a positive number")
elif nT == 1:
   print("First",nT,"Fibonacci number(s):")
   print(n1)
else:
    print("First",nT,"Fibonacci number(s):") 
    while count < nT:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1