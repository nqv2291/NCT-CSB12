print("Enter a text: ", end='')
string = input()
if(string == string[::-1]):
      print("This is a palindrome.")
else:
      print("This is not a palindrome.")