['red', 'green', 'blue', 'yellow', 'orange',
    'purple', 'pink', 'brown', 'black', 'white']
print('Color list:')
ans = ''
for color in color_list:
    ans += color + ', '
print(ans[:-2])
n = int(input('Input position: '))
print(f'Color at position {n}: {color_list[n - 1]}')
