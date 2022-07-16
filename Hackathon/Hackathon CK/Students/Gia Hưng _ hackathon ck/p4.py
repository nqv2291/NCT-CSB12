

order_list = []

def morefood():
    getmore =  input("Great choice sir/madam! Anything else? (y/n) ")
    if getmore == "y":
        getfood()
    elif getmore == "n":
        print("Thank you for ordering!")
        getlist()

def morefood2():
    getmore =  input("Anything else? (y/n) ")
    if getmore == "y":
        getfood()
    elif getmore == "n":
        print("Thank you for ordering!")
        getlist()

def getfood():
    orders = input("Please choose a dish: ")
    if orders in order_list:
        print("You have already chosen this dish, anything else? ")
        morefood2()
    else:
        order_list.append(orders)
        morefood()

def getlist():
    print("your order:")
    for i in order_list:
        print(i)

order1 =input("Please choose a dish: ")
order_list.append(order1)
morefood()






        

