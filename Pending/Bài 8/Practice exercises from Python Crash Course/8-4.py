# ở bài này, hàm được thêm giá trị mặc định là
# size mặc định là "large"
# message mặc định là "I love Python"
def make_shirt(size="large", message="I love Python"):
    print(f"Your shirt of size {size} goes with a message: {message}")


## Tạo 1 shirt với size "large" và message "I love Python"
# Ko cần nhập tham số nào vì đây là các giá trị mặc định
# Python sẽ tự động giúp mình nhập là make_shirt("large", "I love Python")
make_shirt()

# Tạo 1 shirt với size "medium" và message "I love Python"
# Chỉ cần nhập size, bỏ qua message
# Python sẽ tự động giúp ta nhập là make_shirt("medium", "I love Python")
make_shirt("medium")
# nó sẽ giống với make_shirt(size="medium")
# sở dĩ anh có thể ko cần ghi size= vì Python có thể tự nối giá trị này với giá trị đầu tiên
# của phần định nghĩa theo Position Arguments (vì nó đều ở vị trí đầu tiên trong phần arguments)

# Tạo 1 shirt với size và message bất kì, cụ thể: size là "Tiny", message là "Tui là người tí hon"
make_shirt("Tiny", "Tui là người tí hon")
# Anh cần phải nhập cả 2 tham số trong trường hợp này vì cả 2 tham số cần nhập đều ko phải là giá trị mặc định,
# nên Python sẽ không giúp ta nhập nữa.