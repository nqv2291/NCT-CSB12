a = int(input("Number of items:"))
non_value = 0
lists = [[] for i in range(a)]
for s in range(a):
    b = input("Item")
    lists[s].append(b)
    c = input ("Price")
    lists[s].append(int(c))
for s in range (a):
    non_value = lists[s][1] + non_value
non_value /= a
print (f"average price is {non_value}")
print (f"Food that are over average price:")
for s in range (a):
    if lists[s][1] > non_value:
        print (lists[s])
    else: 
        continue

