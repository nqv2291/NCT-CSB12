


evennum = int(input("enter your number"))

def even(evennum):
    if( evennum % 2 == 0):
        print(f"{evennum} is even")
    else:
        print(f"{evennum} not even")

even(evennum)

radius = int(input("enter your radius"))

def call_area(radius):
    area = 0
    area = radius*3.14
    print(f"your area is: {area}")

call_area(radius)

strings = input("enter your text")
def reverse(strings):
    reverse = strings[::-1]
    print(f"your text reversed: {reverse}")

reverse(strings)


palastring = input("enter your text") 
def pali_check(palastring): 
    reversepali = palastring[::-1] 
    if (palastring == reversepali): 
        print(f"{palastring} is a palindrome") 
        
pali_check(palastring)