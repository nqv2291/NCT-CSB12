lst = ["Blue", "Green", "Purple", "Gray"]
nLST = [""]
print("Color list: ")
for i in lst:
    print(i,end=" ")
print("")

print("""Delete using word or number:
    Press 1 to delete using word
    Press 2 to delete using number""")

b = input()
if b == 1:
    c = input("Item to delete: ")
    nLST = lst.remove(c)
else:
    c = int(input("Item to delete: "))
    nLST = lst.pop(c + 1)