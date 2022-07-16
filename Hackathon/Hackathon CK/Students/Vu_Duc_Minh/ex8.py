def printFibo(nT):
    n1 = 0
    n2 = 1
    count = 0
    if nT == 1:
        print(f"First fibonacci number: {n1}")
    else:
        print("First",nT,"Fibonacci number(s):") 
        while count < nT:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

nT = int(input("Enter a number: "))
while nT <= 0:
    nT = int(input("Please enter a positive number: "))
printFibo(nT)