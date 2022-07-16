def palindrome_checker(string):
    return "This is a palindrome." if string == string[::-1] else "This is not a palindrome."


string = input('Input a text: ')
print(palindrome_checker(string))
