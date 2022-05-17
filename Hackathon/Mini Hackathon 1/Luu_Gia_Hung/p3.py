number1 = int(input("enter a number"))
if(number1 > 13):
    print(f"{number1} is larger than 13")
else:
    print(f"{number1} is not larger than 13")

number2 = int(input("enter a number"))
if(number2 % 2 == 0):
    print(f"{number2} is even")
else:
    print(f"{number2} is not even")

month = int(input("enter a month"))
if(month <= 7):
    if(month % 2 == 0):
        print(f"this month has 30 days")
    elif(month == 2):
        print(f"this month has 28 days")
    else:
        print(f"this month has 31 days")
if(month > 7):
    if(month % 2 == 0):
        print(f"this month has 31 days")
    else:
        print(f"this month has 30 days")
if(month > 12):
    print("not a month")

    