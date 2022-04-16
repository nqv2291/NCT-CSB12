# Anh tạo 1 hàm tên make_shirt.
# Hàm này cần 2 tham số là size và message 
# (tham số tức là các giá trị (input) được nhập khi gọi hàm)
def make_shirt(size, message):
    print(f"Your shirt of size {size} goes with a message: {message}")

# Gọi hàm make_shirt bằng cú pháp <tên hàm>(<tham số>)
# ở đây, anh nhập 2 tham số theo như phần define bên trên bao gồm size và message
# size là 15, message là chuỗi "I love Python"
make_shirt(15, "I love Python")

"""
Notes:
- Có 2 bước chính trong thao tác với hàm: tạo hàm, sử dụng hàm
+ tạo hàm: def <tên hàm>(<các tham số>):
                ... phần thân hàm
+ sử dùng hàm: <tên hàm>(<các tham số>)
- Nếu không có phần gọi hàm thì hàm sẽ không chạy
"""