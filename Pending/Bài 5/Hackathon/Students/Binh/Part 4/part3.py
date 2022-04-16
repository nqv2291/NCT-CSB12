import re
email = input("Input youe email: ")
email = re.search ('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
if email:
    print("Email is validate")
else:
    print("Wrong email")
