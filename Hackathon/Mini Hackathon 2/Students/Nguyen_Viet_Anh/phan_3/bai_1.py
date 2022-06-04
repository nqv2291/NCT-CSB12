lst = [ 5 ,1 , 8, 92, -1, 30]
a = int(input("Input a number: "))

if a in lst:
    count = lst.index(a)
    count += 1
    print(f"Number found at position: {count}")
else:
    print("Number not found")