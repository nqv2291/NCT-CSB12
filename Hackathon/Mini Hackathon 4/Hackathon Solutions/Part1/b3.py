computers = {'HP': 20,
             'DELL': 50,
             'MACBOOK': 12,
             'ASUS': 30
             }

# 3.1 Read
print("All products in stock:")
for product, num in computers.items():
    print("{:<7}: {}".format(product, num))

# 3.2 Sum value
sum = sum(computers.values())
print(f"Total number of products: {sum}")

# 3.3 Create (3)
computers['FUJITSU'] = 15
computers['ALIENWARE'] = 5