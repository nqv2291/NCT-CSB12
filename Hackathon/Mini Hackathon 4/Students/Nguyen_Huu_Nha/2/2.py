Comp = {'HP': 20,
'DELL': 50,
'MACBOOK': 12,
'ASUS': 30}
a = input ("Input a brand")
b = input ("Input amount")
Comp.update({a: b})
print ("Available products:")
for key, value in Comp.items():
    print(f"{'- {}'.format(key)}: {value}")