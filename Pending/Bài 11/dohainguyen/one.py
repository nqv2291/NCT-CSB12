from dict import storage

print("Available MACBOOK:",storage["MACBOOK"])

brand=input('input a brand: ')
print(f"Available{brand}: {storage[brand]}")