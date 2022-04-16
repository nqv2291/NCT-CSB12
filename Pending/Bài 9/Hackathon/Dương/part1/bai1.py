def evenCheck(x): return True if x%2==0 else False

num = int(input("Enter a number: "))
print(f"{num} is an even number") if evenCheck(num) == True else print(f"{num} is not an even number")
