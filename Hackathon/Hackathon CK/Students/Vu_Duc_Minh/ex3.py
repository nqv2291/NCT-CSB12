def palindrome(n):
    lst = []
    string = ''
    for i in n:
        lst.append(i)
    lst.reverse()
    for x in lst:
        string += x
    if string == n:
        return True
    else: 
        return False

n = input("Input a string: ")

if palindrome(n):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")