from turtle import circle


def cal_area(r):
    S = r ** 2 * 3.14
    return S
n = float(input("Input radius: "))
a = cal_area(n)
print(f"Circle's area: {a}")