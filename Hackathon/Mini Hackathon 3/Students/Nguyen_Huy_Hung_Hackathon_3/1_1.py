def isEven(s: int) -> bool:
    return s % 2 == 0
if isEven(int(input('Input a number: '))):
    print("This number is even")  
else:
    print("This number is not even")