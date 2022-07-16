phone_price = {
    "Iphone12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000
}

n =  int(input("Input your budget:"))

for key, value in phone_price.items(): 
    if value <= n:
        print(f"- {key}: {value}")
