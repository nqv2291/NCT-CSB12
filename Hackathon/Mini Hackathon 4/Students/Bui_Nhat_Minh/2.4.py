laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

sum_lap = 0
for brand in laptops:
    sum_lap += laptops[brand]
print(f"Total product: {sum_lap}")
