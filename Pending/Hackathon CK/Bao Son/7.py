from operator import length_hint


number = [5, 1, 8, 92, -1, 30]
lenth = len(number)
print(number)

for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (number[i] > number[j]):
            tmp = number[i]
            number[i] = number[j]
            number[j] = tmp
 
print(number)