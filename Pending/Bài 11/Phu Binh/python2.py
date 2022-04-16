#Bai 1
from multiprocessing import Value
from operator import length_hint
from traceback import print_tb


brand = {
     'HP': '20',
  'DELL': '50',
  'MACBOOK': '12',
  'ASUS': '30'
}
print("Available products:")
for key in brand.keys():
    print(key + ":" +brand[key])
   

#Bai 2
brand = {
    'HP': '20',
  'DELL': '50',
  'MACBOOK': '12',
  'ASUS': '30'
}
brad=(input("Input a brand: "))
Amnt=(input("Input amount: "))
print("Available products:")
brand[brad]=Amnt
for key in brand.keys():
    print(key + ":" +brand[key])


print("_________")
#Bai 3
a_dict = {
    'HP': 20,
  'DELL': 60,
  'MACBOOK': 2,
  'ASUS': 30
}
values = a_dict.values()
total = sum(values)
print("Total products: ", total )
#for key in brand.keys():
 #   print(key + ":" +brand[key])