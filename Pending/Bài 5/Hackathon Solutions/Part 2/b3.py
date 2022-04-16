# get input
while True:
    num = int(input("Enter n (n>0): "))
    if num > 0:
        break

print(f"The ODD sequence from {num} to 0 is: ", end="")

# Check whether n is odd or even
if num % 2 == 0:
    num = num - 1

# print the sequence from 0 to n
for i in range(num, 0, -2):
    print(i, end=" ")