from audioop import reverse


name= input("Input a test: ")
Reverse = name[::-1]
if name== Reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")