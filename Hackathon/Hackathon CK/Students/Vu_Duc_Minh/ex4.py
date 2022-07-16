print("== Welcome to the Restaurant ==")

boo = False
l = []
while boo is False:
    q = ""
    a = input("Please choose a dish: ")
    if a in l:
        q = input("You have already chosen this one. Anything else? ")
    else:
        q = input("Great choice! Anything else? ")
        l.append(a)
    if (q == 'n'):
        print("Well done! Your order:")
        for i in l:
            print(f"- {i}")
        boo = True