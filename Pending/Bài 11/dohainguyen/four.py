from dict import price
from dict import storage

print("Total price:",price["ASUS"]*5)

brand=input("Input a brand: ")
amount=int(input("Input amount to buy: "))

print("Total price:",price[brand]*amount)

storage[brand]=storage[brand]-amount

print("Available products:")
for key in storage:
    print(f"-{key}: {storage[key]}")
