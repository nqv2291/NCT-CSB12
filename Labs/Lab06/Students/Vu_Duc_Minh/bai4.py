steak = ('Ribeye Steak', 30.5)
salad = ('Potato Salad', 5)
wine = ('Sparkling Wine', 7)
salmon = ('Smoked Salmon', 12)
soup = ('Chicken Soup', 8.5)
cake = ('Tiramisu', 4.5)
lst = [steak,salad,wine,salmon,soup,cake]
lstA = 0
for i in lst:
    lstA += i[1]
lstAvg = lstA / len(lst)  
print("Number of items:",len(lst))
for x in lst:
    print("Item",lst.index(x)+1,":",x[0])
    print("Price of item",lst.index(x)+1,":",x[1])
    print("")
print("Average menu price:",lstAvg)
for ix in lst:
    if ix[1] > 11.25:
        print("Item(s) above average price:",ix)
