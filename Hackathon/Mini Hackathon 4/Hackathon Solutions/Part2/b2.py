product_quantities = {'HP': 20,
                    'DELL': 50,
                    'MACBOOK': 12,
                    'ASUS': 30,
                    'TOSHIBA': 10,
                    'FUJITSU': 15,
                    'ALIENWARE': 5
                    }

product_price = {'HP': 600,
                'DELL': 650,
                'MACBOOK': 12000,
                'ASUS': 400,
                'TOSHIBA': 600,
                'FUJITSU': 900,
                'ALIENWARE': 1000
                }

# merge product_quantities and product_price -> computers
computers = {}
for p in product_quantities.keys():
    sum = product_price[p] * product_quantities[p]
    computers[p] = {'quantity': product_quantities[p],
                    'price': product_price[p],
                    'subvalue': sum
                    }

# Calculate price
total_price = 0
print("Value of all products of each brands:")
for product, info in computers.items():
    val = info['subvalue']
    total_price += val
    print(f"- {product}: {val}")
print(f"Total price: {total_price}")
