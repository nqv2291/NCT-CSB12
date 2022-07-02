Comp = {'HP': 20,
'DELL': 50,
'MACBOOK': 12,
'ASUS': 30}
Comp.update({'DELL': 60})
Comp.update({'MACBOOK': 2})
print ("Available products:")
for key, value in Comp.items():
    print(f"{'- {}'.format(key)}: {value}")