input_string = input("Enter a string: ")

def check_palindrome(args):
    if args == args[::-1]:
        return True
    else:
        return False

if check_palindrome(input_string) == True:
    print("String "+ "'" + input_string + "'" + " is a Palindrome")
else:
    print("String "+ "'" + input_string + "'" + " is not a Palindrome")



        