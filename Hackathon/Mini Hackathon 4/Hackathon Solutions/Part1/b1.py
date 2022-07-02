# 1.1 init dictionary
computers = {'HP': 20,
             'DELL': 50,
             'MACBOOK': 12,
             'ASUS': 30
             }

# 1.2 Read (1)
print(f"Number of MACBOOK left in stock: {computers['MACBOOK']}")

# 1.3 Read (2)
user_input = input("Check for number of available product: ")

if user_input not in computers:
    print("This product is unavailable.")
else:
    print(f"Number of {user_input} left in stock: {computers[user_input]}")