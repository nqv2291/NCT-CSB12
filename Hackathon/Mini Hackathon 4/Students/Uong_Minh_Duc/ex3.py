#1+2+3
shop={
    "HP":600,
    "DELL":650,
    "MACBOOK":1200,
    "ASUS":400,
}
print("price of asus:",shop["ASUS"])
brand=input("input a brand:")
price=shop.get(brand)
print("price of",brand.upper(),":",price)
