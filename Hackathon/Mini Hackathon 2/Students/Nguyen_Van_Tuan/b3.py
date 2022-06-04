# 1. 
nums_list = [594739150, 758158430, 337320200, 173373530, 731296610]
nums = int(input('Input a number: '))
for i in range(len(number_list)):
    if number_list[i] == nums:
        print(f'Number found at position {i + 1}')
        break
else:
    print(f'Number not found')
# 2. 
nums_list = [594739150, 758158430, 337320200, 173373530, 731296610]
print(f'Sum of all numbers: {sum(nums_list)}')
# 3. 
print('Input the list of numbers.')
print('Enter 0 to finish.')
number_list = [594739150, 758158430, 337320200, 173373530, 731296610]
while True:
    nums = int(input())
    if nums == 0:
        break
    number_list.append(nums)
print(f'Sum of numbers in list: {sum(nums_list)}')