#bai1
def is_int(num):
    if num%int(num)==0:
        return True
    else:
        return False



#bai2

def is_prime(num):
    i=0
    if num<=1:
        return False
    if num>1:
        if num<4:
            return True
        else:
            for number in range (2,num):
                if num%number==0:
                    return False
                else:
                    i = i+1
                    if i==num-2:
                        return True
                    




#bai4
def giai_thua(num):
    if num==0 or num==1:
        return (1)
    if num>1:
        a=1
        for number in range (num,1,-1):
            val=a*number
            a=val
        return (val)
