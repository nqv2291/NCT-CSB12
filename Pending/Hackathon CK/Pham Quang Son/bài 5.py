phones = {
    "Iphone12": "28000000",
    "SamsungN10": "16000000",
    "Oppo 93": "7500000",
    "Vsmart": "7400000",
    "Vivo": "4200000"
}
phone_price = [phones["Iphone12"],phones["SamsungN10"],phones["Oppo 93"],phones["Vsmart"]]
phone_name = input("input name of a phone: ")
print(f"Price of {phone_name}:",phones[phone_name])
budget = input("input your budget: ")
for value in phones.values:
    if budget >= value:
        print(phones.values)