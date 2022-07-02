dict = {
    'HP': 600,
'DELL': 650,
'MACBOOK': 1200,
'ASUS': 400,
}
a = input("Input a brand: ")
b = input ("Input amount to buy: ")
print (f"total price = {dict[a] * int(b)}")
