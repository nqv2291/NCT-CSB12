def facCal(n):
    fac = 1
    if n < 0:
        return "Factorial doesn't exist."
    elif n == 0:
        return 1
    else:
        for i in range(1,n+1):
            fac = fac*i
        return fac

n = int(input("Please enter a number: "))
print(f'The factorial of the inputed number is {facCal(n)}')

    