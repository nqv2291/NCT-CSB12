from dict import storage

storage2 = storage.copy
storage2["TOSHIBA"]=10

print("Available products:")
for key in storage2:
    print(f"-{key}: {storage2[key]}")

brand=input('Input a brand: ')
amounnt=input("Input amount: ")
storage2[brand]=amounnt

print("Available products:")
for key in storage2:
    print(f"-{key}: {storage2[key]}")

storage2["DELL"]=60
storage2["MACBOOK"]=2

sum=0
for key in storage:
   sum=sum+storage[key]
print("Total products:",sum)


