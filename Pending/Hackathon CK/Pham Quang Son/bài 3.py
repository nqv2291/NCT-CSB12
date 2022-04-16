def isPalindrome(a):
    return a == a[::-1]
a = input("input a text: ")
ans = isPalindrome(a)
if ans:
    print("this is a palindrome")
else:
    print("This is not a palindrome")