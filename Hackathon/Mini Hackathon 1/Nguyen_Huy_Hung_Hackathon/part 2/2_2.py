n = int(input("Input a number: "))
while not (n > 0):
    print("Error, please enter a positive number")
    n = int(input("Input a number: "))
else:
    for i in range(0, n+1):
        print(i)