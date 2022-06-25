
lap = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}

lap['TOSHIBA'] = 10

print("Available products: ")

for key, value in lap.items(): 
    print("-", key + ":", value)