number = int(input("Input a number: "))
count = 0
while(number != 0):
    number = number // 10
    count += 1 
print(f"This number has {count} digit(s).")