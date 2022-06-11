# 1.1 
def test(num):
    if num % 2 == 0:
        return True
    else:
        return False


check = int(input('Input a number: '))
if test(check):
    print('This number is even')
else:
    print('This number is not even')
# 1.2 
def area(radius):
    return 3.14 * radius ** 2


unit = float(input('Input radius: '))
print("Circle's area:", area(unit))
# 1.3 
def reverse(str):
    return str[::-1]


answer = input('Input a text: ')
print('Reversed text:', reverse(answer))
# 1.4
def palidrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


answer = input('Input a text: ')
if palidrome(answer):
    print('This is a palidrome.')
else:
    print('This is not a palidrome.')