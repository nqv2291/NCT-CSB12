#1+2
# shop={
#     "HP":600,
#     "DELL":650,
#     "MACBOOK":1200,
#     "ASUS":400,
# }
# print("price of asus:",shop["ASUS"])
# print("total price of 5 asus's:",shop["ASUS"]*5)
# brand=input("input a brand:")
# stock=int(input("input amount to buy:"))
# price=shop.get(brand)
# print("total price of",stock,"",brand,"'s" ":",price*stock)
#3
shop={
    "HP":600,
    "DELL":650,
    "MACBOOK":1200,
    "ASUS":400,
}
def function():
    brand=input("input a brand:")
    stock=int(input("input amount to buy:"))
    price=shop.get(brand)
    print("total price of",stock,"",brand,"'s" ":",price*stock)
