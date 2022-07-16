phone_price = {
    "Iphone 12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000,
}
input("Our store's list of phones : Iphone 12 , Samsung N10 , Oppo 93 , Vsmart , Vivo ")
namephone = input("Enter the name of the phone to see the price: ")
if(namephone in phone_price):
    print(f"Price of a {namephone} is : {phone_price[namephone]}")
else:
    print("Sorry we don't have the phone that you are looking for")

def checkbudget():
    budget = int(input("input your budget"))
    print("Phones that fit your budget:")
    for x in phone_price:
        if budget > phone_price[x]:
            name = x
            price = phone_price[x]
            print(f"{name}: {price}")

checkbudget()

