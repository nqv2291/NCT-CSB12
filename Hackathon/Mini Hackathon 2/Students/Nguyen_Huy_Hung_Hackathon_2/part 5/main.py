name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT" ]
number = [247100, 333300, 266800, 420900, 318000]
print(f"""Indices of:
- Most populated dist.: {number.index(max(number))}
- Least populated dist.: {number.index(min(number))}""")
print(f"""Names of:
- Most populated dist.: {name[number.index(max(number))]}
- Least populated dist.: {name[number.index(min(number))]}""")