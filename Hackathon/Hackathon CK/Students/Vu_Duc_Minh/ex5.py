dic = {
    "iphone12": 28000000,
    "samsungn10": 16000000,
    "oppo93": 7500000,
    "vsmart": 7400000,
    "vivo": 4200000
}

def nameInput(a):
    if a in dic:
        print(f"Price of phone: {dic[a]}")
    else:
        print("This phone doesn't exist.")

def budgetInput(b):
    budget = int(b)
    lst = {}
    for i in dic:
        if budget >= dic[i]:
            lst[i] = dic[i]
    return lst

b = input("Please input budget: ")
t = budgetInput(b)
print(t)


# a = input("Please input phone's name: ")
# a.lower()
# nameInput(a)