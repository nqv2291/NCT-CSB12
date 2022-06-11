def palidrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


user_string = input('Input a text: ')
if palidrome(user_string):
    print('This is a palidrome.')
else:
    print('This is not a palidrome.')
