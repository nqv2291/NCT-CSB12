def reverse_string(x):
      return x[::-1]

text = input("Enter a string: ")
rev_text = reverse_string(text)

if text == rev_text:
    print(f"string {text} is a Palindrome")
else:
    print(f"string {text} is not a Palindrome")

