arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Original list:\t{arr}')

main_arr = arr.copy()
for i in range(len(main_arr)):
    main_arr[i] += 2
print(f'Add 2:\t\t{main_arr}')

main_arr = arr.copy()
for i in range(len(main_arr)):
    main_arr[i] *= 2
print(f'Muliply by 2:\t{main_arr}')

main_arr = arr.copy()
for i in range(len(main_arr)):
    main_arr[i] = arr[(i+2) % len(main_arr)]
print(f'Shift 2:\t{main_arr}')
