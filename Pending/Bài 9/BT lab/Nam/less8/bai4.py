from modules import*

num=int(input("Input number:"))
a=0

for number in range (1,num+1):
    sum=a+(giai_thua(number)/number)
    a=sum

print(f"Result: {sum}")
    

