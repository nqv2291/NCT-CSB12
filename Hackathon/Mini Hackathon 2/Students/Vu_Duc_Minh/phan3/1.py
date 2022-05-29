lst = [1,6,78,-11,401,99]
a = int(input("Please input a number: "))
for i in lst:
    if a == i:
        b = lst.index(a)
        print("Number found at position:", b+1)
        break
    else:
        print("Number not accurate.")
        