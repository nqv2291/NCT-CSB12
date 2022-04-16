from modules import*

num=float(input("Input number: "))

if is_int(num):
    print(f"{int(num)} is an interger")
else:
    print(f"{(num)} is not an interger")