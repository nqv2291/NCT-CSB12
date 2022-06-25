#2.1
computer_ammount = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}

computer_ammount["Toshiba"] = 10
print(conputer_amount)
#2.2
brandname = input("Input a brand")
ammount = int(input("Input ammount"))
computer_ammount[brandname] = ammount
print(computer_ammount)
#2.3
computer_ammount["Dell"] = 60
computer_ammount["Macbook"] = 2
#2.4
sum = 0
for i in computer_ammount.values():
    sum = sum + i
print(f"total product: {sum}")