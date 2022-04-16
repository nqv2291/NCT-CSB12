def sap_xep_tang_dan(numbers):
     
    lenth = len(numbers)
 
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (numbers[i] > numbers[j]):
                x = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = x
 
    return numbers

numbers = [1, 5, 3, 2, 4, -1, -2, -3, -4]
print(numbers)
new_list = sap_xep_tang_dan(numbers)
print(new_list)


### sauce: freetuts.net