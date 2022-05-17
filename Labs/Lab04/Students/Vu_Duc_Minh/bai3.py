num = int(input("Please input a number: "))
res = 1
while num < 0:
    print("Please reenter a number that's greater than 0 ", end="")
    num = int(input("Please input a number: "))
if num == 0:
    print(res)
else:
    for i in range(2, num + 1):
        res *= i
    print(res)

