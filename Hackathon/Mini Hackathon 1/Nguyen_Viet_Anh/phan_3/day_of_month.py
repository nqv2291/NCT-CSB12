#Cach 1:
#input
from math import e


n = int(input("Input a month: "))
while n > 12:
    n = int(input("Input a month: "))
#check

#month = 1
if(n == 1):
    print("This month has 31 days")
    quit()
#month = 2
if (n == 2):
    print("This month have 28 or 29 days")
    quit()
#month 3-7
if (n % 2 == 0) and (n <= 7):
    print("This month has 30 days")
    
else:
    print("This month has 31 days")
    quit()
#month 7-12
if(n % 2 == 0) and (n > 7):
    print("This month has 31 days")
    quit()
else:
    print("This month has 30 days")


#cach 2 
if n == 2:
    print("This month have 28 or 29 days")
elif (n == 6) or (n == 4) or (n == 9) or (n == 11):
    print("This month has 31 days")
else:
    print("This month has 30 days")