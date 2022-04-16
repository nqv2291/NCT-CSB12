#funtion to check palindrome
def check_palindronme(string):
    str1 = string[::-1]
    if str1==string:
        return True
    else:
        return False

string = input("input string:  ")
if check_palindronme(string):
    print(f"{string} is a palindrome")
else: 
    print(f"{string} is not a palindrome")