prices = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

laptops = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

asus = prices.get("ASUS")
print(f"Total price: {asus * 5}")

inp = prices.get(input("Input a brand: "))
amount = int(input("Amount to buy: "))
print(f"Total price: {inp * amount}")

brand = input('Input a brand: ')
amount = int(input('Input amount to buy: '))
print(f"Total price: {prices[brand] * amount}")
laptops[brand] -= amount
print('Available products: ')
for brand, amount in laptops.items():
    print(f"- {brand}: {amount}")