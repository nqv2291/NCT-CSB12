print('Deposit: ', end='')
deposit = int(input())

RATE = 1.05
print('Account after 1 year: ', deposit*RATE)
print('Account after 2 years: ', deposit*RATE**2)
print('Account after 10 years: ', deposit*RATE**10)