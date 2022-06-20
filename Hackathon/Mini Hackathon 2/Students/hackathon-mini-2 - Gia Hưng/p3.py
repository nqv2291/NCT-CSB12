numberlist= [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
inputnum = int(input("input your number"))
if((int(inputnum) in numberlist) == True):
    thenum = numberlist.index(inputnum)
    print(thenum)
else:
    print("not found")

numberlist2 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
number = 0
for i in numberlist:
    number = i + number
print(number)

i = 1
number2 = 0
while i > 0:
    sumnum = int(input("get number"))
    number2 = sumnum + number2
    if(sumnum == 0):
        print(number2)
        break