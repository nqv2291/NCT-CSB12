#bài 1
shop = {
    "HP":"20",
    "DELL":"50",
    "MACBOOK":"12",
    "ASUS":"30",
}
print("HP: ",shop["HP"])
print("DELL: ",shop["DELL"])
print("MACBOOK: ",shop["MACBOOK"])
print("ASUS: ",shop["ASUS"])
#bài 2:
print("Available MACBOOKs: ",shop["MACBOOK"])
#bài 3:
a = input("input a brand: ")
if a in shop:
    print(f"Available {a}s: ",shop[a])
else:
    print("the shop doesn't have this brand")
    