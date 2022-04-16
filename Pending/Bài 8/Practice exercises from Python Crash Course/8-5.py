# tạo 1 hàm gồm 2 tham số: name, country
# tham số country có giá trị mặc định là Vietnam
def describe_city(name, country="Vietnam"):
    # Mục đích duy nhất của hàm là in ra một câu: <tên thành phố> ở nước <tên nước>
    print(f"{name} is in {country}")

# Dùng hàm để viết ra dòng: Hanoi is in Vietnam
# Vì Vietnam là giá trị mặc định nên anh không cần nhập tham số này vào
describe_city("Hanoi") # Python sẽ giúp chúng ta gõ 1 dòng tương đương là: describe_city("Hanoi", "Vietnam")

# Dùng hàm viết ra dòng: Da Nang is in Vietnam
describe_city("Da Nang")

# Dùng hàm viết ra dòng: Bangkok is in Thailand
# Vì Thailand không phải là giá trị mặc định nên ta cần nhập đầy đủ cả 2 tham số theo định nghĩa của hàm ở phần def
describe_city("Bangkok", "Thailand")