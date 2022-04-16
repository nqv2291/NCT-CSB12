def integer(a):
    if int(a)==a:
        print(f"{a} is an integer.")
    else:
        print(f"{a} is not an integer. ")
n=float(input("Input a number: "))
integer(n)