#1+2+3
shop={
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30,
}
print("macbook available:",shop["MACBOOK"])
brand=input("input a brand:")
print(brand.upper(),"available:",shop[brand.upper()])
