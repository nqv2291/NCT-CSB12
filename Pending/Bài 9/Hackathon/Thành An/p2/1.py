input_number = int(input("Enter a number: "))

def factorialCalculate():
    factorial = 1
    for i in range(1, input_number + 1):
        factorial = factorial * i
    print("Factorial:", input_number, "! =", factorial)

factorialCalculate()