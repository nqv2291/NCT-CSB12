username = input("Tên đăng nhập: ")
email = input("Nhập email: ")
password = input("Mật khẩu: ")
repass = input("Nhập lại pass: ")

while password != repass:
    print("Mật khẩu chưa đúng")
    repass = input("Nhập lại pass: ")
