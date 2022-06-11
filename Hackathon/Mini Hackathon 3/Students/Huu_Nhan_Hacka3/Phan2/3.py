a = int(input("Number?"))
Fibbo_list = [1,1]
def print_fibbo(n):
    for i in range(n-2):
        b = Fibbo_list[i] + Fibbo_list[i+1]
        Fibbo_list.append(b)
    return Fibbo_list
print ("First 5 Fibonacci ")
print (*print_fibbo(a), sep = ", ")