def is_Palindrome(a):
    return a == a[::-1]


a = input("Input a text: ")
b = is_Palindrome(a)

if b:
    print("This is a palindrome")
else:
    print("This is not a palindrome")