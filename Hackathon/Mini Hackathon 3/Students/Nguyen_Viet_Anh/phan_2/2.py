def sap_xep_tang_dan(numbers):
    lenth = len(numbers)

    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (numbers[i] > numbers[j]):
                # Hoán đổi vị trí
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
    return numbers


numbers = [5,1,8,92,-1,30]

print("Mảng trước khi sắp xếp")
for i in range(len(numbers)):
    print(numbers[i], end=" ")

print()

print("Mảng sau khi sắp xếp")

a = sap_xep_tang_dan(numbers)

for y in range(len(a)):
    print(a[y], end=" ")
