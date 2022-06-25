#1.1 
laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
#1.2
print(f"Available MACBOOKs: {laptops['MACBOOK']}")
#1.3
brand = input('Input a brand: ')
print(f"Available {brand}s: {laptops[brand]}")
