# reverse a string - using string slicing
def reverse_str(inp_str):
  return inp_str[::-1]

# reverse a string - using loop
def reverse_str_v2(inp_str):
  result_str = ''
  for ch in inp_str:
    result_str = ch + result_str
  return result_str

# get user input
print('Input a text: ', end='')
text = input()

# print result
print('Reversed text:', reverse_str(text))
print('Reversed text:', reverse_str_v2(text))