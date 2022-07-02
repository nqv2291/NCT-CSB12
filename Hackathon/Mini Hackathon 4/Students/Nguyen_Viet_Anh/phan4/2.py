lap = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 1200,
    'ASUS' : 400,
}
vip = input("Input a brand: ")
value = lap[vip]

nub = int(input("Input amount to buy: "))

value *= nub

print("Total price: ", value)