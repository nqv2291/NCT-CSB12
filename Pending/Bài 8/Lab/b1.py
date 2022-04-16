# function check for integer
def is_int(n):
    """
        Hàm này sẽ kiểm tra số n có phải là số nguyên hay không bằng cách so sánh nó với giá trị của nó sau khi bị ép kiểu nguyên (int)
        Ta sẽ dùng giá trị của dòng n == int(num) để làm giá trị trả về (return value)
        Sẽ có 2 trường hợp xảy ra:
            1. Giả sử n là số thực, ví dụ 3.14. 
            Lúc này ta có: n = 3.14
                            int(n) = 3 (vì hàm int() sẽ ép số n thành một số nguyên, tức là ép 3.14 thành 3)
                => n == int(n) lúc này sẽ có giá trị False (vì n = 3.14, int(n) = 3, rõ ràng là 3.14 != 3) 
            
            2. Giả sử n là số nguyên, ví dụ 10.
            Lúc này ta có: n = 10.0
                            int(n) = 10 (vì từ ban đầu, n đã là số nguyên rồi nên giá trị của n sẽ ko có thay đổi gì)
                => n == int(n) lúc này sẽ có giá trị True (vì nó ko đổi gì mà: n = 10, int(n) vẫn là 10, nên là 10 bằng 10 là đúng)
    """
    return n == int(n)


# Đây là phần thân chương trình-----------------------------------------------------------------------------
# Anh lấy input từ người dùng rồi ép kiểu sang số thực (float)
num = float(input("Input number: "))

# Dùng if else để kiểm tra số này có nguyên hay ko
# is_int(num) là hàm kiểm tra số num có phải số nguyên hay không bằng cách:
# + Nếu num là số nguyên: is_int(num) = True (như đã giải thích ở phần hàm bên trên)
# + Nếu num ko phải là số nguyên: is_int(num) = False 
if is_int(num):
    # vào được đây chứng tỏ is_int(num) = True, hay nói cách khác, num là số nguyên
    print(f"{int(num)} is an integer")
else:
    # Vào trong này tức là is_int(num) = False -> num là số thực
    print(f"{num} is not an integer")