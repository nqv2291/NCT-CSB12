a = int(input("Input a number: "))
b = a % 3
c = a % 5
if b == 0 and c == 0:
    print("This number can be divided by 5 and 3.")
elif b == 0 and c != 0:
    print("This number can be divided by 3 but not 5.")
elif b != 0 and c == 0:
    print("This number can be divided by 5 but not 3.")
else:
    print("This number can not be divided by 5 and 3")
