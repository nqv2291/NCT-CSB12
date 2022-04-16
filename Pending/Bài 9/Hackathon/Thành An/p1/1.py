num = int(input("Enter a number: "))

def odd_even():
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is not an even number")

odd_even()