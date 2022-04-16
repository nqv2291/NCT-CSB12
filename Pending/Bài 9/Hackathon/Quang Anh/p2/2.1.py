def giai_thua(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    print(n,'! =',fac)    
a=input('nhập số:')
a=int(a)
if a > 0:
    s=giai_thua(a)
else:
    print('invalid')    