phones={"Iphone12":28000000,"Samsung N10":16000000,"Oppo 93":7500000,"Vsmart":7400000,"Vivo":4200000 }

phone=input("Input a name of a phone: ")
if phone not in phones:
    print(f"No {phone} here")
if phone in phones:
    print(f"Price of {phone}:{phones[phone]}")
### {phones[phone]} is the value of the key




money = int(input("how much do u have"))
for phone in phones:
    if money <= phones[phone]:
        print(phones)
else:
    pass

