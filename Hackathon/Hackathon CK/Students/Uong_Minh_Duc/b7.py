# c:dem
# s:sort
# i:lap
list=[5,1,8,92,-1,30]
emptylist=[]
def sort(s):
    while s:
        c=s[0]
        for i in s:
            if i<c:
                c=i
        emptylist.append(c)
        s.remove(c) 
    return emptylist
print("un-sorted list:",list)
print("sorted list:",sort(list))