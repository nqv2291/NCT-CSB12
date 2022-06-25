compu_ammount = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}

compu_price = {
    "HP" : 600,
    "Dell" : 650,
    "Macbook" : 1200,
    "Asus" : 400
}

input(f"total price: {compu_price['Asus']*5}")

computer_buy = input("input brand")
ammount_buy = int(input("input ammount"))
total_price = compu_price[computer_buy]*ammount_buy
print(f"tota price{total_price}")

compu_ammount[computer_buy] = compu_ammount[computer_buy] - ammount_buy

print(compu_ammount)