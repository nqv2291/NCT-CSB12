
# get input
n = int(input("Input a positive number: "))

# generate the fibonacci list
print(f"First {n} Fibonacci number(s): ", end="")

# initialize first 2 elements
fibo = [0,1] 

for i in range(n):
    if i >= 2:
        fibo.append(fibo[i-1]+ fibo[i-2])
    print(fibo[i], end= " ")


                    