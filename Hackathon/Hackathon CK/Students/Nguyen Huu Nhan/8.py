fibo = [1,1]
c = int(input("Input a number?: "))
for i in range(c-2):
    fibo.append(fibo[i+1]+fibo[i])
print(f"First {c} Fibonacci numbers", *fibo, sep=' ')

    