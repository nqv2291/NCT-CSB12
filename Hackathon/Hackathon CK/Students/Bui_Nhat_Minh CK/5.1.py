phone_price = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000
}

phone = input('Input name of a phone: ')
if phone in phone_price:
    print(f"Price of {phone}: {phone_price[phone]}")
else:
    print("We currently don't have that type of phone.")
