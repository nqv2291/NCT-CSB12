end = int(input("Input a number: "))
for num in range(1, end + 1):
    if num % 2 != 0:
        print(num, end = " ")