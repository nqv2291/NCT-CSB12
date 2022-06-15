def sortList(nums: list):
    mini, maximum = float('inf'), float('-inf')
    for num in nums:
        if num > maximum:
            maximum = num
        if num < mini:
            mini = num
    from collections import Counter
    counter = Counter(nums)
    result = []
    for i in range(mini, maximum+1):
        if i in counter:
            result.extend([i] * counter[i])
    return result
print(f"Original list: {[5, 1, 8, 92, -1, 30]}\nSorted list: {sortList([5, 1, 8, 92, -1, 30])}")