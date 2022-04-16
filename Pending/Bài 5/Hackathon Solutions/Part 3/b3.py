# get input
while True:
    month = int(input("Enter a month: "))
    if (month > 0) and (month < 13):
        break
    else:
        print("Please enter a valid month from 1 to 12")

# Find number of days in month
if (month == 4) or (month == 6) or (month == 9) or (month == 11):
    print("\nThis month has 30 days")
elif month == 2:
    print("\nThis month has 28 or 29 days depend on the year is a leaf year or not")
else:
    print("\nThis month has 31 days")

