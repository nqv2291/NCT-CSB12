def isPalindrome(s):
     
    rev = "".join(reversed(s))
 
    if (s == rev):
        return True
    return False

s = input("a word to check: ")
ans = isPalindrome(s)
 
if ans:
    print("This is palindrome")
else:
    print("This is not palindrome")


## sauce: geeksforgeeks