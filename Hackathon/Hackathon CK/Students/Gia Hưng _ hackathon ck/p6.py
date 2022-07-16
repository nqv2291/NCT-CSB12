num = int(input("input your number: "))
num_show = num
count = 0

while num != 0:
    num //= 10
    count += 1

print(f"{num_show} has {count} digits")