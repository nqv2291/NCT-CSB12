def isPalindrome(s):
    return s == s[::-1]

s = input("Input a text: ")
ans = isPalindrome(s)

if ans:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")