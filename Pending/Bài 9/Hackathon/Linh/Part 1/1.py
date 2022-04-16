def even_num (n):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if even_num(num):
    print(f"{num} is an even number")
else: 
    print(f"{num} is not an even number")