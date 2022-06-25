laptops_price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

brand = input('Input a brand: ')
amount = int(input('Input amount to buy: '))
print(f"Total price: {laptops_price[brand] * amount}")
