from dict import price
from dict import storage
sum=0 

print("Total value of availabe brands:")
for key in storage:
    print(f"-{key}: {storage[key]*price[key]}")
    sum=sum+storage[key]*price[key]
    
print("Total value of availabe items:",sum)
