# Sử dụng module math bằng cách gõ cú pháp dưới đây
import math
# Nếu gõ theo cách này, mỗi lần dùng một hàm gì đó trong module math thì phải gõ math.<tên hàm>
# Ví dụ dùng hàm sqrt để tính căn bậc 2 của 35: math.sqrt(35)

# Hàm này tên là is_prime, tham số là num
# Hàm này sẽ trả về True nếu num là số nguyên tố, ko phải nguyên tố sẽ trả về False
# "Trả về" tức là:
# + Nếu num là số nguyên tố: is_prime(num) =  True
# + Nếu num ko phải nguyên tố: is_prime(num) = False
def is_prime(num):
    # Dòng này giúp loại những số chắc chắn ko phải là nguyên tố
    # Những số âm, số 0, số 1 đều ko phải số nguyên tố
    # Vi vậy nếu num mà là một trong những số đó thì sẽ trả về False
    # Ví dụ: num = 1 -> is_prime(num) = False
    # Lưu ý: Khi hàm đã return, thì hàm sẽ kết thúc, phần còn lại của hàm sẽ ko đc chạy nữa!!!
    if num < 2:
        return False # Chạy nốt dòng 18 này là dừng luôn nè, ko chạy cái hàm is_prime() này nữa

    # Nếu mà nó vẫn chạy tiếp tới đây chứng tỏ num >= 2, nghĩa là nó chưa return False ở trên kia và phần for dưới đây sẽ đc chạy
    for n in range(2, num):
        # Có một công thức để kiểm tra 1 số có phải số nguyên tố ko, đó là nếu mà số đó ko chia hết cho bất cứ số nào từ 2 đến giá trị của nó 
        # thì sẽ đc coi là 1 số nguyên tố.
        # Vì vậy, anh dùng hàm for để lấy các giá trị của n là 2, 3, 4, ..., num-1
        # Ví dụ: số cần xét là num = 5, ta có các giá trị của n cần xét là: 2, 3, 4.
        if num % n == 0:
            return False # Chương trình sẽ trả về False ngay lập tức nếu số num chia hết cho bất cứ số nào đang xét
            # ở ví dụ trên, num = 5, vì num ko chia hết cho bất cứ số nào trong nhóm đc xét là 2, 3, 4 nên phần return False này sẽ ko đc chạy
            # Nếu giả sử num=4, khi n = 2 thì 4 chia hết cho 2 nên sẽ return False và hàm dừng lại tại đây
    
    # Nếu vẫn chạy được tới đây chứng tỏ vòng for đã kết thúc, chương trình ko tìm đc số n nào để num chia hết cho n.
    # điều này chứng tỏ num ko có ước nào trong các số (2, 3, 4... num-1)
    # hay nói cách khác, num chỉ có 2 ước là 1 và chính nó, vì vậy hàm return True 
    return True

# get input
num = int(input("Input number: "))

# print result
if is_prime(num):
    # Nhảy vào đây nếu is_prime(num) =  True, tức là hàm is_prime() return True, hay nói cách khác thì num là 1 số nguyên tố
    print(f"{num} is a prime")
else:
    # Nếu chạy phần này tức là is_prime() trả về False
    print(f"{num} is not a prime")