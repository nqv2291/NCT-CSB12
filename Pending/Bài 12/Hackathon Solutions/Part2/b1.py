# 1.1 init price table
computer_price = {'HP': 600,
                  'DELL': 650,
                  'MACBOOK': 12000,
                   'ASUS': 400,
                   'TOSHIBA': 600,
                   'FUJITSU': 900,
                   'ALIENWARE': 1000
                   }


# 1.2 Print price
print(f"Price of an ASUS: {computer_price['ASUS']}")

# 1.3 Print price (2)
product = input("Search for price of product: ")

if product not in computer_price:
    print("This product is unavailable.")
else:
    print(f"Price of a(n) {product}: {computer_price[product]}")
