arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Original list:{arr}')

new_arr = arr.copy()
for i in range(len(new_arr)):
    new_arr[i] += 2
print(f'Add 2:{new_arr}')

new_arr = arr.copy()
for i in range(len(new_arr)):
    new_arr[i] *= 2
print(f'Muliply by 2:{new_arr}')

new_arr = arr.copy()
for i in range(len(new_arr)):
    new_arr[i] = arr[(i+2) % len(new_arr)]
print(f'Shift 2:{new_arr}')

