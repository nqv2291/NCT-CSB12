print("""Input the list of numbers.
Enter 0 to finish.""")
list = []
sum = 0
while True:
    inp = int(input())
    list.append(inp)
    if inp == 0:
        break

for i in range(len(list)):
    sum += list[i]
print(f"Sum of numbers in list: {sum}")