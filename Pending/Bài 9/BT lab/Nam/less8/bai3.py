from modules import*
import itertools

num=int(input("Input numer:"))
prime_list=[]

print("check1")
for number in itertools.count(start=0):
    print("check2")
    if is_prime(number):
        print("in1")
        prime_list.append(str(number))
    if len(prime_list)==num:
        print("innnnnnnnnnnn")
        break
print("check3")
primes=" ".join(prime_list)
print(f"First {num} prime(s):{primes}")
