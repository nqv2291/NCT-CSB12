print ("== Registration ==")
username = input("Username: ")
password = input("Password: ")
repeat_pass = input("Repeat your password:")
while not (repeat_pass == password):
    print ("Passwords do not match. Please input again.")
    repeat_pass= input("Repeat your password again:")
    
email = input("Email:")
if password == "12345" and username == "admin" and email == "abc@gmail.com":
    print ("Registered successfully.")