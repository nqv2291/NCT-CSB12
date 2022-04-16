# Bai 1
from ctypes.wintypes import HPALETTE


Brand = {
    'HP': 20,
  'DELL': 50,
  'MACBOOK': 12,
  'ASUS': 30
}
print("Available MACBOOKs:", Brand['MACBOOK'])
brat=(input("Input a brand: "))
if brat == ('HP'):
  print("Available: ", Brand['HP'])
elif brat ==('DELL'):
  print("Available:", Brand['DELL'])
elif brat ==('MACBOOK'):
  print("Available:", Brand['MACBOOK'])
else:
    print("Available:", Brand['ASUS'])