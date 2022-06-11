def fibonacci(n):
    a = 0
    b = 1
    c = 1
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            a = b
            b = c
            c = a + b
        return c

input = int(input("Input a number: "))
sb = ""
for i in range(1, input + 1):
    sb = sb + " " +str(fibonacci(i))
print(sb)