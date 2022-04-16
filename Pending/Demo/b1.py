arr = list(range(10))

arr_add_2 = [ele + 2 for ele in arr]
arr_mul_2 = [ele*2 for ele in arr]
arr_shift_2 = arr[2:] + arr[:2]

print(arr, arr_add_2, arr_mul_2, arr_shift_2, sep = "\n")