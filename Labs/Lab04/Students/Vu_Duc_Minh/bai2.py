a = float(input("Please input a positive number: "))
while a < 0:
    print("Please try again with an actual positive number! ", end="")
    a = float(input())
if a > 0:
    print("Thank you.")


