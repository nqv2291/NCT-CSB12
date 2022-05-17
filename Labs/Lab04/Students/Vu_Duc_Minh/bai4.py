inputString = input("Input anything: ")
total = 0
for i in inputString:
    if i.isdigit():
        tInt = int(i)
        total += tInt
    else:
        print("not a digit")
print(total)

    
