#1+2
# shop={
#     "HP":20, 
#     "DELL":50, 
#     "MACBOOK":12, 
#     "ASUS":30, 
#     "TOSHIBA":10,
# }
# print("available product:",shop)
# brand=input("input a brand:")
# stock=input("input number amount:")
# shop.setdefault(brand.upper(),stock)
# print("updated available product:",shop)

#3+4
shop={
    "HP":20, 
    "DELL":60, 
    "MACBOOK":2, 
    "ASUS":30, 
}
print("total products:",sum(shop.values()))


