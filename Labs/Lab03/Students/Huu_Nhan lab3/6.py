a = input("number?")
b = input("number?")
c = input("number?")

if a > b and a > c:
    if b + c < a:
        print ("this is a triangle")
    else:
        print("not triangle")
elif b > a and b > c:
    if a + c < b:
        print ("This is a triangle")
    else:
        print("not triangle")
elif c > a and c > b:
    if c > a + b:
        print ("Its a triangle")
    else:
        print("not triangle")