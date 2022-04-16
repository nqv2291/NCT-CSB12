def fibo(x):
    if x == 1:
        return 0
    elif x ==2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

num = int(input("Enter a number: "))        
print(f"First {num} elements of fibonacci sequence: ", end="")
for i in range(1,num + 1):
    print(fibo(i),end=" ")
                    