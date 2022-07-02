lap = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
}

lap['DELL'] = 60
lap['MACBOOK'] = 2

for key, value in lap.items(): 
    print("-", key + ":", value)