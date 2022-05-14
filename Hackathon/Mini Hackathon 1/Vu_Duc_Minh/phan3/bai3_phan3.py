a = int(input("Please input the month: "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("The inputed month has 31 days")
elif a==2:
    print("The inputed month has 28 or 29 days")
elif a==4 or a==6 or a==9 or a==11:
    print("The inputed month has 30 days")
else:
    print("The inputed number is not a month.")
    
