a = int(input('Input number: '))
if a % 3 == 0:
    if a % 5 == 0:
        print(f"{a} is divisible by 3 and 5")
    else:
        print(f"{a} is divisible by 3")
else:
    if a % 5 == 0:
        print(f"{a} is divisible by 5")
    else:
        print(f"{a} is not divisible by 3 or 5")
