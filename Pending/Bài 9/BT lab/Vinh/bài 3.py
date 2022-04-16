def prime(a):
    card=1
    if n<2:
        card=0
        return card 
    for i in range (2,int(a**1/2)+1):
        if n%i==0:
            card=0 
            break
    return card 

n=int(input("Input a number: "))




       

