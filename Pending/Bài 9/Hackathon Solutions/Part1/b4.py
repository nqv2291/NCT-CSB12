# return True if string is Palindrome
def check_palindrome(s):
    return s == s[::-1]

# get input
s = input("Enter a string: ")

# print result
if check_palindrome(s):
    print(f"String \"{s}\" is a Palindrome")
else:
    print(f"String \"{s}\" is not a Palindrome")
