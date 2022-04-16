##CHECK IF A NUMBER IS PRIME
print("program to check if a number is a prime or not\n")
#create function
def is_prime(num):
    if num==1:
        print("1 is not a prime")
    else:
        for x in range(2,num):
            if num%x==0:
                print(f'{num} is not a prime')
                exit()
        
        print(f"{num} is a prime")
#check
num = int(input("input number:  "))
is_prime(num)