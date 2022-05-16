print('== Registration ==')
print()
username = input('Username: ')
print()
password = input('Password: ')
while len(password) < 8:
    print('Invalid password. Please input again.')
    password = input('Password: ')
repeat_password = input('Repeat Password: ')
while repeat_password != password:
    print('Passwords not match. Please input again.')
    repeat_password = input('Repeat Password: ')
print()
email = input('Email: ')
while '@' not in email or '.' not in email:
    print('Invalid email. Please input again.')
    email = input('Email: ')
print()
print('Registered successfully.')
