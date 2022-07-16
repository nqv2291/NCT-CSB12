while True:
    try:
        num1 = int(input('Input first number: '))
        num2 = int(input('Input second number: '))
    except:
        print('I only understand integer.')
        continue
    else:
        break
print(f"{num1} + {num2} = {num1 + num2}")
