# initialize original list
arr = list(range(10))

# construct new arrays
arr_add_2 = [el + 2 for el in arr]
arr_mul_2 = [el * 2 for el in arr]
arr_shift_2 = arr[2:] + arr[:2]

# output the constructed arrays
print('Original list :', arr, end='\n\n')
print('Add 2         :', arr_add_2)
print('Multiply by 2 :', arr_mul_2)
print('Shift 2       :', arr_shift_2)