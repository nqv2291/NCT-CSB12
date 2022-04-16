num=[-1,2,15,20,4]
sum=0
number=int(input("Input a number: "))
if num.count(number) == True:
    print("Number found at position",num.index(number)+1)
else:
    print("Number not found ")
for i in range(0,len(num)):
    sum=sum + num[i]
print("Sum of all numbers:",sum)
print("input a list of number")
print("enter 0 to stop")
while True:
    new=int(input("intput a number: "))
    if new == 0:
        break
    else:
        num.append(new)
for i in range(0,len(num)):
    sum=sum + num[i]
print("Sum of numbers in list:",sum-80)
