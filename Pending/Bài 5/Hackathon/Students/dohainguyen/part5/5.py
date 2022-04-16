import random
points=0
while points>=0:
    print("points:",points)
    b = random.randint(0,50)
    a = random.randint(0,50) 
    c=random.randint(1,2)   
    if c ==1:
        print(f'{a} - {b}=')
        n=float(input("input result: "))
        if n== a-b :
            print("correct")
            points=points+1
        else: 
            print('wrong')
            print('game over')
            quit()
    else:
        print(f'{a} + {b}=')
        n=float(input("input result: "))
        if n== a+b :
            print("correct")
            points=points+1
        else: 
            print('wrong')
            print('game over')
            quit()
