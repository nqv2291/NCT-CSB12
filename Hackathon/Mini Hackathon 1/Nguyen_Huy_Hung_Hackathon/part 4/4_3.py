print ("== Registration ==")
username = input("Username: ")
password = input("Password: ")
while (len(password) < 8):
    print("Invalid password. Please try again.")
    password = input("Password: ")

repeat_pass = input("Repeat your password: ")
while not (repeat_pass == password):
    print ("Passwords do not match. Please input again.")
    repeat_pass= input("Repeat your password again:")
    
email = input("Email: ")
while '@' not in email or '.' not in email:
    print('Invalid email. Please input again.')
    email = input('Email: ')

print ("Registered successfully.")