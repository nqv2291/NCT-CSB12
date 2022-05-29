print ("""Input the list of numbers.
Enter 0 to finish.""")
list = []
b = 0
while True:
    inpu = input("")
    list.append(inpu)
    if inpu == str(0):
        break
for i in list:
    b += int(i)
print (f"Sum of all numbers: {b}")

