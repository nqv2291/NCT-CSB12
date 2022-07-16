from audioop import reverse


a = input ("Text input:")
def is_palindrome():
    b = list(a)
    c = list(reversed(a))
    if b == c:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")
is_palindrome()


