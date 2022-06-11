lst = [5,1,8,92,-1,30]
def lstSorter(n):
    lst2 = []
    while n:
        min = n[0]
        for i in n:
            if i < min:
                min = i
        lst2.append(min)
        n.remove(min)
    return lst2
print(f'Pre-sorted list: {lst}')
print(f'Sorted list: {lstSorter(lst)}')