# get input
while True:
    num = int(input("Enter n (n>0): "))
    if num > 0:
        break

# print the sequence from 0 to n
print(f"The sequence from 0 to {num} is: ", end="")
for i in range(num+1):
    print(i, end=" ")