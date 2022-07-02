laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

laptops['DELL'] = 60
laptops['MACBOOK'] = 2

print('Available products:')
for brand, amount in laptops.items():
    print(f"- {brand}: {amount}")
