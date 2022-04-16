def haha(a):
    Fibonacci=[0,1]
    a>0
    if a==1:
        print([0])

    if a==2:
        print([0,1])
    else:
        for i in range (0,a-2):
            Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
        return Fibonacci

m=int(input("Input a number: "))
val=haha(m)
print(f"list {m} số fibonacci đầu tiên là {val}")

