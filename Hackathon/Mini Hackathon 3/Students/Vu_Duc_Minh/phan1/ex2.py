def areaCal(n):
    c = float(n ** 2)
    a = float(c * 3.14)
    return a

n = float(input('Input radius: '))
print(f"Circle's area: {areaCal(n)}")