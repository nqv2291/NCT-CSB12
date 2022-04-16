# check if a string is a palindrome
def is_palindrome(inp_str):
  n = len(inp_str)
  for i in range(n//2):  # loop over inp_str
    if inp_str[i] != inp_str[n-i-1]:  # if found an unmatched pair
      return False                    # => not palindrome
  return True  # passed all pairs => is palindrome

# get user input
print('Input a text: ', end='')
text = input()

# print result
if is_palindrome(text):
  print('This is a palindrome')
else:
  print('This is not a palindrome')