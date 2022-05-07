# pre-assigned username and password
USERNAME = 'admin'
PASSWORD = '12345'

# get input
print('Welcome to The Ultimate Sercurity System')
print('Username: ', end='')
username = input()
print('Password: ', end='')
password = input()

# check conditions
if username == USERNAME and password == PASSWORD:
  print(f'You are logged in, {username}.')
else:
  print(f'Wrong username or password.')