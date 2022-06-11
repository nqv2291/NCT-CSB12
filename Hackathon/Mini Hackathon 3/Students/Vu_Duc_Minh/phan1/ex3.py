def reverseStr(n):
    lst = []
    string = ''
    for i in n:
        lst.append(i)
    lst.reverse()
    for x in lst:
        string += x
    return string

n = input("Please input a string: ")
print(f"Your reversed string: {reverseStr(n)}")

