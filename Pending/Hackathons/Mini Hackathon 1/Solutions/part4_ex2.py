# get user inputs
print('== Registration ==\n')

# get username
print('Username: ', end='')
username = input()

# get password
print('\nPassword: ', end='')
password = input()
while True:
  print('Repeat password: ', end='')
  if input() == password:
    break
  else:
    print('Passwords not match. Please input again.')

# get email
print('\nEmail: ', end='')
email = input()

# print result
print('\nRegistered successfully.')
