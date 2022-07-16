numbers = [5, 1, 8, 92, -1, 30]
length = len(numbers)
 
print(f"Original list: \n{numbers}")

for i in range(0, length - 1):
    for j in range(i + 1, length):
        if (numbers[i] > numbers[j]):
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
 
print(f"Sorted list: \n{numbers}")