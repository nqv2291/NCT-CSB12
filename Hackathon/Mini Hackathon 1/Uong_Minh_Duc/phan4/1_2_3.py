print("REGISTRATION SIMULATOR")
username=(input("your username pls:"))
print("your username is:",username)
password=(input("your pass pls:"))
checkpass=(input("repeat your pass pls:"))
while True:
    password=(input("your pass pls:"))
    checkpass=(input("repeat your pass pls:")) 
    if password==checkpass:
        print("your pass is:" ,password)
        break
    else:
        print("pasword not match, try again")
email=(input("your mail pls:"))
print("Registered successfully")
