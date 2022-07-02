lapNub = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}
lapValue = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 1200,
    'ASUS' : 400,
}
vip = input("Input a brand: ")
value = lapValue[vip]

nub = int(input("Input amount to buy: "))

price = value * nub
print("Total price: ", price)

oldNub = lapNub[vip]
newNub = oldNub - nub

lapNub[vip] = newNub

for key, value in lapNub.items(): 
    print("-", key + ":", value)