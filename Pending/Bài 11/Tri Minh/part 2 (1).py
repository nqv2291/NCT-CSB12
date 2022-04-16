shop_items = {"MACBOOK": 12, "HP": 20, "DELL": 50, "ASUS": 30}
add = input("Input your brand: ")
num = input("Input your amount: ")
shop_items[add] = num
print("Available products:")
for key in shop_items.keys():

    print("-", key, ":", shop_items[key])
