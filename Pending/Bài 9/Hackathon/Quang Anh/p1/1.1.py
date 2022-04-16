def so_chan(num):
    return num % 2 == 0
a=input('nhập số: ')
a=int(a)
if so_chan(a):
    print(a,'là số chẵn.')
else:
    print(a,'không là số chẵn.')