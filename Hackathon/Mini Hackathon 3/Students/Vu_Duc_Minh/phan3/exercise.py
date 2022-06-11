import msvcrt
import os

a1 = ['P', '-', '-', '-', '-', '-', '-']
a2 = ['-', '-', '-', '-', '-', '-', '-']
a3 = ['-', '-', '-', '-', '-', 'K', '-']
a4 = ['-', '-', '-', '-', '-', '-', '-']
a5 = ['D', '-', '-', '-', '-', '-', '-']

print(a2.index('P'))

# def mapGeneration():
#     print(' '.join(a1))
#     print(' '.join(a2))
#     print(' '.join(a3))
#     print(' '.join(a4))
#     print(' '.join(a5))

# mapGeneration()

# def movementInput():
#     ch = msvcrt.getche().decode('utf-8')
#     while ch != 'a' and ch != 'w' and ch != 's' and ch != 'd' and ch != 'W' and ch != 'S' and ch != 'D' and ch !='A':
#         print("")
#         print("Please input either 'W','A','S','D'")
#         ch = msvcrt.getche().decode('utf-8')
    
#     if ch == 'd' or ch == 'D':
#         playerPos = a1.index('P')
#         a1.insert(playerPos+1, 'P')
#         a1.append(a1.pop(0))



