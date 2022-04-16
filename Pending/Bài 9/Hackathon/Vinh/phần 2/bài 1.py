def giai_thừa(a):
    tich=1
    for i in range (1,a+1):
        tich=tich*i
    return tich
n=int(input("Input a positive number: "))
m=giai_thừa(n)
print(f"Factorial {n}! is {m}")