#Bai 5
list = {
   "Iphone 12": 28000000,
   "Samsung N10": 16000000,
   "Oppo 93": 7500000,
   "Vsmart": 7400000,
   "Vivo": 1200000,
   "Iphone12": 28000000,
   "SamsungN10": 16000000,
   "Oppo93": 7500000,
   "Vsmart": 7400000,
   "Vivo": 1200000
}
x = input("Input a Phone: ")
print("Price of smartphone:", list[x])

#part 2
list = {
    "Iphone 12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000
}
  

K = int(input("Ïnput your budget: "))
  

res = {}
for key in list:
    
   
    if not (isinstance(list[key], int) and list[key] > K):
        res[key] = list[key]
          

print("Phones that fit your budget: " + str(res), sep='n') 


#Bai 6
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)

#Bai 7
list = [5, 1, 8, 92, -1, 30]
print("Original List: ")
print(list)
list.sort()
print(list)

#Bai 8
nterms = int(input("Input a number: "))
n1, n2 = 0, 1
count = 0
 
if nterms <= 0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1