numIn = int(input("Number of items: "))
numReal = 1

lst = []
tup = ()

sum = 0

lstPrice = []
while numReal <= numIn:
    addItem = input(f"Item {numReal}: ")
    addPrice = float(input(f"Price of item {numReal}: "))
    newTUP= tup + (addItem,addPrice)
    lst.append(newTUP) 
    lstPrice.append(addPrice)
    numReal += 1


#average
for i in lstPrice:
    sum = sum + i
average = sum / numIn
print(f"Average price: {average}")


#Item(s) above average price
place = []
for y in lstPrice:
    if y > average:
        float(y)
        place.append(y)

for item in lst:
    if place in item:
        print (item)
# phan 2 no la lam 

