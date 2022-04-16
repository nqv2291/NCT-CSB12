#bài 1:
Number = [5, 1, 8, 92, -1, 30]
a=int(input("input a number: "))
for i in range(len(Number)):
        if (a in Number):
                print("number found at position ", i-1)  
        else:
                print("number not found")