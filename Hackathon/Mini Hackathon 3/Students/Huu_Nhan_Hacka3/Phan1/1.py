a = int(input("Number?"))
def even(num):
    if num % 2 == 1:
        return False
    else:
        return True
if even(a):
     print(f'{int(a)} is an even')
else:
    print(f'{a} is not an even')