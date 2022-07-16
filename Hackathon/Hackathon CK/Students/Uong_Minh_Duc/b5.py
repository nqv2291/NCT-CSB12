shop={
    "Iphone12":28000000,
    "SamsungN10":16000000,
    "Oppo93":7500000,
    "Vsmart":7400000,
    "Vivo":4200000,
}
# print("Program 1")
# name=input("input a name of a phone:")
# price=shop.get(name)
# print("price of",name.upper(),":",price)
print("Program 2")
def closest(shop,budget):
    closest=shop[0]
    shop=str(shop)
    for i in range(1,len(shop)):
        if (i-budget)<closest:
            closest=i
    return closest
budget=input("input your budget")
closest(shop,budget)


