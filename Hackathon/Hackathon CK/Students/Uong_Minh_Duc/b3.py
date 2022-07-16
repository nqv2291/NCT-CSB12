text=str(input("input a text:"))
def is_palindrome(text):
    if text==text[::-1]: 
        return "This is palindrome"
    else: 
        return "This is not a palindrome"
print(is_palindrome(text))