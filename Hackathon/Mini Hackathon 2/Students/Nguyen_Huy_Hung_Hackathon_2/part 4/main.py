init = [5, 1, 8, 92, 7, 30, 23, 43, 55, 29, 21, 44]
even = []
for i in range(len(init)):
    if init[i] % 2 == 0:
        even.append(init[i])
print("Even numbers:", end=" ")
for a in even:
    print(a, end=" ")
print("\n")
list = []
while True:
    inp = int(input())
    list.append(inp)
    if inp == 0:
        break
for a in list:
    if a % 2 == 0:
        print(f'Even numbers in list: {a}')