# return sorted list
def sort_list(nums):
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                (nums[i], nums[j]) = (nums[j], nums[i])
    return nums

# init number list
numbers = [122, 21, -11, -90, 64, 12]
print(f"The original list: {numbers}")

# sort the given list
sort_list(numbers)

# print sorted list
print(f"The sorted list:   {numbers}")
