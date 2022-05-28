print('Input the list of numbers.')
print('Enter 0 to finish.')
number_list = []
while True:
    n = int(input())
    if n == 0:
        break
    number_list.append(n)
even_list = list(filter(lambda x: x % 2 == 0, number_list))
print('Even numbers in list:', end=' ')
for n in even_list:
    print(n, end=' ')
