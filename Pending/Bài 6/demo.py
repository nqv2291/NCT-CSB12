a = [10, 12, 14, 16]
b = a[:]
# list -> mutable

t = tuple(10, 12, 14, 16)
t = (10, 12, 14, 16, 17)
# tuple -> immutable

print(f"a = {a}, b = {b}")

t.clear()

print(f"a = {a}, b = {b}")

