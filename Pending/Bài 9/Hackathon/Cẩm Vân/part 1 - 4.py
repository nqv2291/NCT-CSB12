def check_palindrome(x):
    if x == x[::-1]:
        return True

string = input("Enter a string: ")
if check_palindrome(string):
    print(f"String '{string}' is a Palindrome")
else:
    print(f"String '{string}' is not a Palindrome")    