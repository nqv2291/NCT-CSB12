#function to check even
def even_num(num):
    if num%2==0:
        return True
    else:
        return False

num = float(input("input number:  "))
if even_num(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is not an even number")    