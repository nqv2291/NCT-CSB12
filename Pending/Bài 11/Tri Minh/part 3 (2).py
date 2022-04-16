from unicodedata import name


price = {"HP": 600, "DELL": 650, "MACBOOK": 650, "ASUS": 400}

brand = input("Input your brand: ")
if brand in price.keys():
    print("price of", brand, ":", price[brand])
