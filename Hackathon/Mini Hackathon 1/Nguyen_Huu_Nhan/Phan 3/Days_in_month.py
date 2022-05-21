Number = int(input("Input a number:"))
if Number == 2:
    print ("This month has 28 days")
elif Number <= 7 and Number % 2 == 0:
    print ("This month has 30 days")
elif Number <= 7 and Number % 2 != 0:
    print ("This month has 31 days")
elif Number > 7 and Number % 2 == 0:
    print ("This month has 31 days")
else: 
    print ("This month has 30 days")