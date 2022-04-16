def check_palindrome(string):
    HV = len(string)
    first = 0
    last = HV -1 
    card  = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               card = 0
               break
    return int(card)  
string = input("Enter the string: ")
card= check_palindrome(string)
if(card):
    print("It is a palindrome ")
else:
    print("This is not a palindrome")
