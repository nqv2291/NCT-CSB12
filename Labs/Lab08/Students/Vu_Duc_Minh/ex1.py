def isInt(num):
    num = float(num)
    a = num % 1
    return a

b = input("Please input something: ")
c = isInt(b)

if c == 0.0:
    print(f'{int(b)} is an integer')
else:
    print(f'{b} is not an integer')