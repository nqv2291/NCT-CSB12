num=[-1,2,15,20,4]
even=[]
for i in range(0,len(num)):
    if num[i]%2==0:
        even.append(num[i])
print("even number in the list:",end=" ")
for i in range(0,len(even)):
    print(even[i], end=" ")
num.clear()
even.clear()
while True:
    new=int(input("intput a number: "))
    if new == 0:
        break
    else:
        num.append(new)
for i in range(0,len(num)):
    if num[i]%2==0:
        even.append(num[i])
print("even number in the list:",end=" ")
for i in range(0,len(even)):
    print(even[i], end=" ")