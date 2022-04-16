###CHECK IF A NUMBER IS A INTERGER OR NOT
print("program to check if a number is a integer or not")
##create a function
def is_num(num):
    if int(num)==num:
        print(f"{int(num)} is a integer")
    else:
        print(f"{num} is not a integer")
##check
num = float(input("input number:  "))
is_num(num)

