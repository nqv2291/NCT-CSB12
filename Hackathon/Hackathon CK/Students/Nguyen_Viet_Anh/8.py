n = int(input("Input a number: "))

n1 = 1
n2 = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("First Fibonacci number is: ",end="")
   print(n1)
else:
   print(f"First {n} Fibonacci numbers: ",end=" ")
   while count < n:
      print(n1 , end=" ")
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1