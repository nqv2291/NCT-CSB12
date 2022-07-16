numA=input("input A:")
numB=input("input B:")
numC=input("input C:")
delta=numB*numB-4*numA*numC;
if(numA==0):
    if (numB==0):
        print("0 solutions");
    else:
        print("Solution:x=+""(",-numC/numB,")")
