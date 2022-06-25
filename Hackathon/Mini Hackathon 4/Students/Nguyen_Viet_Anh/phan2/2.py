lap = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}

vipPro = input("Input a brand: ")
value = int(input("Input amount: "))

lap[vipPro] = value

print("Available products: ")

for key, value in lap.items(): 
    print("-", key + ":", value)