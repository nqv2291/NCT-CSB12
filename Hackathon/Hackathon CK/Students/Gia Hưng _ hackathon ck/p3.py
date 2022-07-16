palastring = input("enter your text: ") 
def pali_check(palastring): 
    reversepali = palastring[::-1] 
    if (palastring == reversepali): 
        print(f"{palastring} is a palindrome") 
        
pali_check(palastring)