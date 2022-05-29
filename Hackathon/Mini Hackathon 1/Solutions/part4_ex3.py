# get user inputs
print('== Registration ==\n')

# == GET USERNAME ==
print('Username: ', end='')
username = input()

# == GET PASSWORD ==
password = None

# check valid password
while True:

  print('\nPassword: ', end='')
  password = input()
  
  has_letter = False
  has_digits = False
  for ch in password:
    if (ch > 'a' and ch < 'z') or (ch > 'A' and ch < 'Z'):  # check if password contained a letter
      has_letter = True
    if ch > '0' and ch < '9':  # check if password contained a digit
      has_digits = True
  
  if has_letter and has_digits and len(password) >= 8:
    break
  else:
    print('Invalid password. Please input again.', end='')

# check matching passwords
while True:
  print('Repeat password: ', end='')
  if input() == password:
    break
  else:
    print('Passwords not match. Please input again.')

# == GET EMAIL ==
email = None

# check valid email
while True:

  print('\nEmail: ', end='')
  email = input()

  if ('.' in email) and ('@' in email):
    break
  else:
    print('Invalid email. Please input again.', end='')

# print result
print('\nRegistered successfully.')
