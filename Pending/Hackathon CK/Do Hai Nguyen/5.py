phone_list={
    "Iphone12":28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}

phone=input("Input name of a phone: ")
print(f"Price of {phone} : {phone_list[phone]}")

balance=int(input("input your budget: "))
for key in phone_list:
    if int(phone_list[key])<=balance:
        print(f"- {key} : {phone_list[key]}")