# return True if num is even, False if num is odd
def is_even(num):
    return num % 2 == 0

# get input
num = int(input("Enter a number: "))

# print result
if is_even(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is not an even number")
