compu_price = {
    "HP" : 600,
    "Dell" : 650,
    "Macbook" : 1200,
    "Asus" : 400
}

print(f"price of Asus: {compu_price['Asus']}")

brand = input("Input your brand")

print(compu_price[brand])