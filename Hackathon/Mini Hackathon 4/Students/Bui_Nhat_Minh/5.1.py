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


print('Total value of available brands:')
for brand in laptops:
    print(f"- {brand}: {laptops[brand] * laptops_price[brand]}")
