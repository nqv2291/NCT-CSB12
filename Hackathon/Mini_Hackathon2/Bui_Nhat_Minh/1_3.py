color_list = ['red', 'green', 'blue', 'yellow', 'orange',
              'purple', 'pink', 'brown', 'black', 'white']
print('Color list:')
ans = ''
for color in color_list:
    ans += color + ', '
print(ans[:-2])
new = input('Input a new color: ')
ans += new
print('New color list:')
print(ans)
