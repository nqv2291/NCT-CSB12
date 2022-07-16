a  ={'Iphone12': 28000000, 'Samsung N10': 16000000, 'Oppo 93': 7500000,
'Vsmart': 7400000,
'Vivo': 4200000}
b = input("Input a name of a phone:")
print (f"Price of {b} = {a[b]}")
c = int(input("Input your budget"))
print ("Phone that fit your budget")
for phones in a:
    if a[phones] < c:
        print(f'-{phones}: {a[phones]}')