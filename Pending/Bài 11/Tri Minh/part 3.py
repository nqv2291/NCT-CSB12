shop_items = {"MACBOOK": 12, "HP": 20, "DELL": 50, "ASUS": 30}

num = input("Input a brand: ")
if num in shop_items.keys():
    print("Avalible", num, ":", shop_items[num])
