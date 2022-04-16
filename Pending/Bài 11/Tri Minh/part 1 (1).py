shop_items = {"MACBOOK": 12, "HP": 20, "DELL": 50, "ASUS": 30}

shop_items["TOSHIBA"] = 10
print("Available products:")
for key in shop_items.keys():

    print("-", key, ":", shop_items[key])
