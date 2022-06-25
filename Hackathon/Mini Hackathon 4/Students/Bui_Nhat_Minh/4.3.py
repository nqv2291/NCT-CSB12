laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

laptops_price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

brand = input('Input a brand: ')
amount = int(input('Input amount to buy: '))
print(f"Total price: {laptops_price[brand] * amount}")

print()
laptops[brand] -= amount
print('Available products:')
for brand, amount in laptops.items():
    print(f"- {brand}: {amount}")
