laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

prices = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

print('Total value of available brands:')
for value in laptops:
    print(f"- {value}: {laptops[value] * prices[value]}")

sum_amount = 0
for value in laptops:
    sum_amount += (laptops[value] * prices[value])
print(f"Total value of available items: {sum_amount}")