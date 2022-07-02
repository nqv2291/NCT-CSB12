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

lapNubList = []
lapValueList = []
c = []
k = -4
for nub in lapNub.values():
    lapNubList.append(nub)

for value in lapValue.values():
    lapValueList.append(value)
    
for i in range(4):
    a = lapNubList[i] * lapValueList[i]
    c.append(a)

for key in lapValue.keys():
    j = c[k]
    lapValue[key] = j
    k+=1

print("Total value of available brands: ")
for key, value in lapValue.items(): 
    print("-", key + ":", value)
# loi