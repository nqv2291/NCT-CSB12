#5.1
computer_ammount = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

lap_price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}


print('Total value of available brands:')
for brand in laptops:
    print(f"- {brand}: {computer_amount[brand] * lap_price[brand]}")
#5.2
sum_price = 0
for brand in computer_ammount:
    sum_price += computer_ammount[brand] * lap_price[brand]
print(f'Total value of available items: {sum_price}')