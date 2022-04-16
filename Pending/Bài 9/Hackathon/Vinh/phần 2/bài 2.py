def sapxep(numbers):
    lenth = len(numbers)


    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (numbers[i] > numbers[j]):
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp

    
    return numbers

n=int(input("Number of numbers you want to input: "))
listnumber=[]

for i in range(0,n):
   n=int(input(f"Input number {i+1}:"))
   listnumber.append(n)

val=sapxep(listnumber)
print(f"list các số từ bé đến lớn là {val}")