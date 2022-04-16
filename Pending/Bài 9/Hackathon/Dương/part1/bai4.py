def check_palindrome(x):
    if x == x[::-1]:
        return True

char = input("Enter a string: ")
if check_palindrome(char):
    print(f"String '{char}' is a Palindrome")
else:
    print(f"String '{char}' is not a Palindrome")    