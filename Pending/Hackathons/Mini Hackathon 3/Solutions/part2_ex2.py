# sort list - selection sort
def sort_asc(arr):
  for i in range(len(arr)-1):
    min_pos = i   # find i-th max element
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_pos]:
        min_pos = j
    arr[i], arr[min_pos] = arr[min_pos], arr[i]  # swap to current position

# initialize list
arr = [5, 1, 8, 92, -1, 30]
print('Original list: ')
for el in arr:
  print(el, end=' ')

# print sorted list
sort_asc(arr)
print('\nSorted list: ')
for el in arr:
  print(el, end=' ')