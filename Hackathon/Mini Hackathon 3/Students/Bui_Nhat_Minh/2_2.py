def custom_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


original_list = [5, 1, 8, 92, -1, 30]
print('Original list:')
print_arr(original_list)
sorted_list = custom_sort(original_list[:])
print('Sorted list:')
print_arr(sorted_list)
