
#Bai 1
prc = {
    'HP': '600',
    'DELL': '650',
    'MACBOOK': '1200',
    'ASUS': '400'
}
#Bai 2
prc = {
    'HP': '600',
    'DELL': '650',
    'MACBOOK': '1200',
    'ASUS': '400'
}
print(prc.get('ASUS'))

#Bai 3
prc = {
    'HP': '600',
    'DELL': '650',
    'MACBOOK': '1200',
    'ASUS': '400'
}
a =(input("Input a brand: "))
if a == ('ASUS'):
   print(prc.get('ASUS'))
elif a == ('HP'):
     print(prc.get('HP'))
elif a == ('DELL'):
     print(prc.get('DELL'))
else:
     print(prc.get('MACBOOK'))

