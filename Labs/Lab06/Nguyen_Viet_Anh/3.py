a = int(input("Input a positive number: "))
b = 1

d = [1,1]
for i in range(1,a + 1):
    d.append(i + b)
    b = i
print(d)

# đoạn đầu ổn mà đoạn sau nó lạ lắm a 