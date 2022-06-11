def evenOrOdds(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("Please input a number: "))
if evenOrOdds(n):
    print("Number is even.")
else:
    print("Number is not even.")