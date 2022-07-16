fibonacci_sequence = [1, 1]


def add_fibonacci(num):
    while len(fibonacci_sequence) < num:
        fibonacci_sequence.append(fibonacci_sequence[len(
            fibonacci_sequence)-2] + fibonacci_sequence[len(fibonacci_sequence)-1])


n = int(input("Input a number: "))
add_fibonacci(n)
print(f"First {n} Fibonacci numbers:", end=" ")
for i in range(n):
    print(fibonacci_sequence[i], end=" ")
