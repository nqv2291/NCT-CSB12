a = input("Input?")
def is_palindrome(word):
    palindrome = word[::-1]
    if word == palindrome:
        return True
    else:
        return False
if is_palindrome(a):
     print("This is a palindrome")
else:
    print('This is not a palindrome')