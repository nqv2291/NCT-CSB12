init = [5, 1, 8, 92, -1, 30]
sum = 0
inp = int(input("Input a number: "))
if inp in init == False:
    print("Number not found")
else:
    print(f"Number found at position {init.index(inp)+1}")

for i in range(len(init)):
    sum += init[i]
print(f"Sum of numbers in list: {sum}")
