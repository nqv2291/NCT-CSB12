compu_ammount = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}

compu_ammount["Toshiba"] = 10

brandname = input("Input a brand")
ammount = int(input("Input ammount"))
compu_ammount[brandname] = ammount
print(compu_ammount)

compu_ammount["Dell"] = 60
compu_ammount["Macbook"] = 2

sum = 0
for i in compu_ammount.values():
    sum = sum + i
print(f"total product: {sum}")