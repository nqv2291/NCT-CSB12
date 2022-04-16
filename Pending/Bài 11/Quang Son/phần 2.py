#bài 1
shop = {
    "HP":"20",
    "DELL":"50",
    "MACBOOK":"12",
    "ASUS":"30",
    "TOSHIBA":"10"
}
print("Available products: ")
print("- HP: ",shop["HP"])
print("- DELL: ",shop["DELL"])
print("- MACBOOK: ",shop["MACBOOK"])
print("- ASUS: ",shop["ASUS"])
print("- TOSHIBA: ",shop["TOSHIBA"])
#bài 2
a = input("input a new brand: ")
b = int(input("input amount: "))
shop[a] = b
for i in len(shop):
    print(shop)