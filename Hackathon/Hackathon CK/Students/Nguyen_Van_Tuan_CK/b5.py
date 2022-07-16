phone = {
    'Iphone 12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000
}

phone_input = input('Input name of a phone: ')
if phone_input in phone:
    print(f"Price of {phone_input}: {phone[phone_input]}")
else:
    print("We currently don't have that type of phone.")



