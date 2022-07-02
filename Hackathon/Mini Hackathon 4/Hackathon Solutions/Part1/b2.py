computers = {'HP': 20,
             'DELL': 50,
             'MACBOOK': 12,
             'ASUS': 30
             }


# 2.1 Create (1)
computers['TOSHIBA'] = 10

# 2.2 Read (2)
print("Add a new product:")
product_name = input("- Product name: ")
product_quantity = int(input("- Number of product: "))

computers[product_name] = product_quantity

# 2.3 Update
computers['DELL'] = 10
computers['MACBOOK'] = 2