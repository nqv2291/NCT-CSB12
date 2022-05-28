lst = ["blue", "red", "teal", "green"]
print("Color list:", ', '.join(lst))
a = input("Item to delete: ")
if a.isdigit():
    a = int(a)
    del(lst[a-1])
elif a.isalpha():
    for i in lst:
        if a == i:
            b = lst.index(a)
            del(lst[b])
print("New list:",lst)
            
