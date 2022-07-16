num = int(input("Please input a number: "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print(f"This number has {count} digits.")