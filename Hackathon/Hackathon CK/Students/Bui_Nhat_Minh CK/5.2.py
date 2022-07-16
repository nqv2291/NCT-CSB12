phone_price = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000
}

while True:
    try:
        budget = float(input("Input your budget: "))
    except:
        print('Please input a number.')
        continue
    else:
        break

budget_phone = []
for phone in phone_price:
    if phone_price[phone] <= budget:
        budget_phone.append(phone)

if len(budget_phone) == 0:
    print('There is no phone that fit your budget.')
elif len(budget_phone) == 1:
    print('Phone that fits your budget:')
    print(f"- {phone}: {phone_price[phone]}")
else:
    print('Phones that fit your budget:')
    for phone in budget_phone:
        print(f"- {phone}: {phone_price[phone]}")
