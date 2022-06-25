#4.1 
computer_ammount = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}
lap_price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

print(f"Total price: {lap_price['ASUS'] * 5}")
#4.2
brand = input('Input a brand: ')
amount = int(input('Input amount to buy: '))
print(f"Total price: {lap_price[brand] * amount}")
#4.3
computer_amount[amount] = computer_amount[amount] - lap_price[brand] * amount
print(computer_amount)