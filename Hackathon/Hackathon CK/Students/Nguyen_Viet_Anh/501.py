phone_price = {
    "Iphone12":28000000,
    "Samsung N10":16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}

name = input("Input name of a phone: ")
print("Price of Vsmart: ", end="")
print(phone_price[name])