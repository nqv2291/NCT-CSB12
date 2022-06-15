def is_Palindrome(s: str):
    if s == s[::-1]:
        return True
    else:
        return False 
if(is_Palindrome(input('Input a text: '))):
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')