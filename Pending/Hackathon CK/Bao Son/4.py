print('Δ Chào mừng đến nhà hàng của chúng tôi Δ')

list = []
while True: 
    dish = input("Mời bạn chọn món: ")

    if dish not in list:
        list.append(dish)
    else:
        print('Bạn đã kêu món này rồi')

    choice = input("Bạn có muốn gọi thêm món không (y/n): ")
    if choice == "n":
        break

print('Danh sách món của bạn: ',list)