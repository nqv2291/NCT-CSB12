n = int(input("Input a number: "))
while not (n > 0):
    print("Error, please enter a positive number")
    n = int(input("Input a number: "))
else:
    for i in range(1, n+1, 2):
        print(i)