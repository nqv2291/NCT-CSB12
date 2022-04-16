#funtion to sort a list
def sort_list(listt):
    listnew =[]
    min=0
    while True:
        min=min(listt)
        listnew.append(min)
        listt.remove(min)
    print(listnew)

list0 = [-29,219,67,0,1,5]
print("the original list is ", list0)
print(f"the new list is ",sort_list(list0))