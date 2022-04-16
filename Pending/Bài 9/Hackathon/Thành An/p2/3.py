input_number = int(input("Enter a number: "))

def print_fibo(input_number):
    print("First " + str(input_number) + " element(s) of fibonacci sequence: ", end=" ")
    a = 0
    b = 1
    for i in range(input_number):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

print_fibo(input_number)
    
    
    