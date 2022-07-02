diction = {'HP': 20,
'DELL': 50,
'MACBOOK': 12,
'ASUS': 30}
dict = {
    'HP': 600,
'DELL': 650,
'MACBOOK': 1200,
'ASUS': 400,
}
a = input("Input a brand")
b = input ("Input amount to buy")
print (f"total price = {dict[a] * int(b)}")
diction[a] -= int(b)
print ("Available products:")
for key, value in diction.items():
    print(f"{'- {}'.format(key)}: {value}")
