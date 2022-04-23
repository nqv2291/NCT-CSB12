# get input
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))

# compare numbers
# initialize max to num1
max = num1
# compare max with num2, num3 to find the larger value if exists
if max < num2:
    max = num2
if max < num3:
    max = num3

print(max)