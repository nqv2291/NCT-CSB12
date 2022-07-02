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

sum_price = 0
for brand in laptops:
    sum_price += laptops[brand] * laptops_price[brand]
print(f'Total value of available items: {sum_price}')
