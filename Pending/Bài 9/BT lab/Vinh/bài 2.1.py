def prime(a):
    for i in range (2, int(a**1/2)+1):
        if a%i==0:
           print(f"{a} is not a prime.")
           
        else:
            print(f"{a} is a prime.")
n=int(input("Input a number: "))
prime(n)