def facto(n): return n*facto(n-1) if n>0 else 1

num = int(input("Enter a number: "))
print(f"Factorial: {num}! = {facto(num)}")