laptops = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

laptops.update({"TOSHIBA": 10})
print("Available products: ")
for key, value in laptops.items():
    print(f"""- {key}: {value}""")

brand = input("Input a brand: ")
amount = int(input("Input amount: "))
laptops.update({brand: amount})
print("Available products: ")
for key, value in laptops.items():
    print(f"""- {key}: {value}""")

laptops.update({"DELL": 60, "MACBOOK": 2})
print("Available products: ")
for key, value in laptops.items():
    print(f"""- {key}: {value}""")

sum_amount = 0
for brand in laptops:
    sum_amount += laptops[brand]
print(f"Total product: {sum_amount}")