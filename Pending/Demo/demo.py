def next_bit_string(b):
    """Generate the next binary string
    in the dictionary order of the
    current string != 111...1"""
    i = len(b) - 1
    while b[i] == 1:
        b[i] = 0
        i -= 1
    if i >= 0:
        b[i] = 1
    
s = "101"
print(s)
b = list(s)
print(b)
next_bit_string(b)
print(b)
print("".join([str(ele) for ele in b]))