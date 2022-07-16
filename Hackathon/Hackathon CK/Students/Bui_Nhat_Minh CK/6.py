while True:
    try:
        num = int(input("Input a number: "))
        if num <= 0:
            raise Exception('non-positive')
    except Exception as e:
        if str(e) == 'non-positive':
            print('Positive number, please.')
        else:
            print('Integer, please.')
        continue
    else:
        break

print(f'This number has {len(str(num))} digit(s).')
