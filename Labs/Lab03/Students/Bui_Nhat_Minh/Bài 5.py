print('Welcome to The Ultimate Sercurity System')
user = input('Username: ')
password = input('Password: ')
if user == 'admin' and password == '12345':
    print('You are logged in, admin.')
else:
    print('Wrong username or password.')
