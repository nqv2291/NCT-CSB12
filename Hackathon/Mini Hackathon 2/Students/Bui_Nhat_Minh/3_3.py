print('Input the list of numbers.')
print('Enter 0 to finish.')
number_list = []
while True:
    n = int(input())
    if n == 0:
        break
    number_list.append(n)
print(f'Sum of numbers in list: {sum(number_list)}')
