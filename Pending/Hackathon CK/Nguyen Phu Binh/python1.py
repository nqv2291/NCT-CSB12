#Bai 1
x = int(input("Input a first number: "))
y = int(input("Input a second number: "))
resh = x + y
print(resh)

#Bai 2
import math 
  
  

def equationroots( a, b, c): 
  
    
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
   
    if dis > 0: 
        print('The equation has 2 solutions:')
        print("x =", (-b + sqrt_val)/(2 * a), "or", "x =", (-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print('The equation has 1 solution:')
        print("x =", -b / (2 * a)) 
      

    else:
        print("Complex Roots") 
        print("x =", - b / (2 * a), " + i", sqrt_val, "or", "x =", - b / (2 * a), " - i", sqrt_val) 


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

  

if a == 0: 
        print("Input correct quadratic equation") 
  
else:
    equationroots(a, b, c)


#Bai 3
def isPalindrome(s):
    return s == s[::-1]
 
 
s = input("Input a word: ")
ans = isPalindrome(s)
 
if ans:
    print("This is palindrome")
else:
    print("This is not palindrome")



