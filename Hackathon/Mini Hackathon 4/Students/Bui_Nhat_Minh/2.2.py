laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

new_brand = input('Input a brand: ')
new_amount = int(input('Input amount: '))
laptops[new_brand] = new_amount
print('Available products:')
for brand, amount in laptops.items():
    print(f"- {brand}: {amount}")
