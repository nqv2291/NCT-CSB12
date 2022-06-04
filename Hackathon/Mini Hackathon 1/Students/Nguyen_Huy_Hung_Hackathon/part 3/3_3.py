from calendar import monthrange as m
m_d = m(2022, int(input("Input a month: ")))
print(f"This month has {m_d[1]} days")