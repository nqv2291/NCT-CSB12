color_list = ['red', 'green', 'blue', 'yellow', 'orange',
              'purple', 'pink', 'brown', 'black', 'white']
print('Color list:')
ans = ''
for color in color_list:
    ans += color + ', '
print(ans[:-2])
de = input('Item to delete: ')

try:
    de = int(de)
    del color_list[de - 1]
    print('New color list:', end=' ')
    ans = ''
    for color in color_list:
        ans += color + ', '
    print(ans[:-2])
except:
    for i in range(len(color_list)):
        if color_list[i] == de:
            del color_list[i]
            print('New color list:', end=' ')
            ans = ''
            for color in color_list:
                ans += color + ', '
            print(ans[:-2])
            break
