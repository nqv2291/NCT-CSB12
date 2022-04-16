arr = list(range(10))

arr_add_2 = [num+2 for num in arr]
arr_mul_2 = [num*2 for num in arr]
arr_shift_2 = arr[2:] + arr[:2]

print(f"Original list : {arr}\n")
print(f"Add 2         : {arr_add_2}")
print(f"Multiply by 2 : {arr_mul_2}")
print(f"Shift 2       : {arr_shift_2}")