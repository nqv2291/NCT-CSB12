print('== Registration ==')
print()
username = input('Username: ')
print()
password = input('Password: ')
repeat_password = input('Repeat Password: ')
while repeat_password != password:
    print('Passwords not match. Please input again.')
    repeat_password = input('Repeat Password: ')
print()
email = input('Email: ')
print()
print('Registered successfully.')
