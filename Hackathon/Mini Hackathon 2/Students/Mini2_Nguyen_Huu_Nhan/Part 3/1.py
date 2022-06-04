list = ['5','1','8', '92', '-1', '30']
input = input("Input a number")
if input in list == False:
    print ("Number not found")
else:
    print (list.index(input)+1)

