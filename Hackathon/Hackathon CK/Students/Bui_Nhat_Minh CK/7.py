list = [5, 1, 8, 92, -1, 30]
print('Original list:')
for i in range(len(list)):
    if i == len(list) - 1:
        print(list[i])
    else:
        print(list[i], end=" ")


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)


def merge(left_half, right_half):
    ans = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            ans.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            ans.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        ans = ans + right_half
    else:
        ans = ans + left_half
    return ans


sorted_list = merge_sort(list)
print("Sorted list:")
for i in range(len(sorted_list)):
    if i == len(sorted_list) - 1:
        print(sorted_list[i])
    else:
        print(sorted_list[i], end=" ")
