print('Numbers with sum of digits = 9:')
a = 1000
d = 10
while d > 0:
    a += 1
    b = str(a)
    c = 0
    for i in range(len(b)):
        c += int(b[i])
    if c == 9:
        print(a, end=' ')
        d -= 1
