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

sum = 0
print("Total value of available brands")
for name in compu_ammount:
    compu_val = compu_ammount[name]*compu_price[name]
    sum = sum + compu_val
    print(f"{name}: {compu_val}")

print(f"total value of all available items: {sum}")

    
  