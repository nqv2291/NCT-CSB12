def sochan(n):
    if (n%2 == 0):
        return True
    else:
        return False
    
input = int(input("Input a number: "))
sochan(input)

if sochan(input):
    print("This number is even")
else:
    print("This number is not even")