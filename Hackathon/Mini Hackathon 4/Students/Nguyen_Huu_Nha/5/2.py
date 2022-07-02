Comp = {'HP': 20,
'DELL': 50,
'MACBOOK': 12,
'ASUS': 30}

diction = {
    'HP': 600,
'DELL': 650,
'MACBOOK': 1200,
'ASUS': 400,
}
a = []
for i in Comp:
    a.append(Comp[i]*diction[i])
print (f"Total value of available items: {sum(a)}")