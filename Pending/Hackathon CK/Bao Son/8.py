n = int(input("Nhập số lượng số đầu tiên của dãy: "))
def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1
    print(100000000000000000000000000)
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

def fibonacci(n):
    print(2000000000000000000000000000)
    if n < 0:
        return -1
    elif (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(n,"số đầu tiền của dãy là:")
for i in range(1, n+1):
    print(fibonacci(i),end=' ')