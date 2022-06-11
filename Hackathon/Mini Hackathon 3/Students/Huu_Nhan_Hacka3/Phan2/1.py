a = int(input("Number?"))
def fuction(num):
    b = 1
    for i in range(1,num+1):
        b = b*i
    return b
print(f"{a}! = {fuction(a)} ")