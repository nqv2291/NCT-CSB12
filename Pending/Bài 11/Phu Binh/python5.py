#Bai 1
brd = {
    'HP': '12000',
    'DELL': '32500',
    'MACBOOK': '14400',
    'ASUS': '12000'
}
print("Total value of \navailable brands:",)
for key in brd.keys():
    print(key + ":" +brd[key])

#Bai 2
brd = {
    'HP': 12000,
    'DELL': 32500,
    'MACBOOK': 14400,
    'ASUS': 12000
}
print("Total value of \n available items", )
values = brd.values()
total = sum(values)
print("Total products: ", total )

