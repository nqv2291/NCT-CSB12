hello = 1
no = 2
no == no - 2 
b = "Admin"
c = "12345678"
print ("Welcome to our Website, we will help to define Data Types")
while no == 2:
    d = input ("Name?")
    if d == b:
        e = input("Pass?")
        if e == c:
            print ("Welcome!")
            while hello == 1:
                a = input("Insert a number")
                if a.isnumeric():
                    if int(a)%2 == 0:
                        print (f"{a} is an even number")
                    else:
                        print (f"{a} is an odd number")
                    if int(a) % 15 == 0:
                        print (f"{a} is divisible by 5 and 3")
                        
                        no = no - 2 
                    elif int(a) % 3 == 0:
                        print (f"{a} is divisible by 3")
                        
                        no = no - 2 
                    elif int(a) % 5 == 0:
                        print (f"{a} is divisible by 5")
                        
                        no = no - 2 
                    else:
                        print (f"{a} is not divisible by 5 or 3")
                        
                        no = no - 2 
                        
                else:
                    try:
                        float(a)
                        if float(a)  // 1 != a:
                            print(f"{a} is a float")
                            
                            no = no - 2 
                    except ValueError:
                        print(f"{a} is a string")
                        no = no - 2 
                S = input ("Again?")
                if S == "yes":
                    hello + 0
                else:
                    print ("Bye!")
                    break
        else:
            print ("Wrong pass!")
    else:
        print ("Wrong username")





