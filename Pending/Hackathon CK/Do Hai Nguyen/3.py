def is_palindrome(str):
    if str == str[::-1]:
        return("this is palidrome")
    else:
        return("this is not palidrome")

string=input("input a text: ")
print(is_palindrome(string))
