init = ['blue', 'white', 'red']
inp = int(input("Input position: "))
print(f"Color at position {inp}: {init[inp-1]}")
del_inp = input("Item to delete: ")
if del_inp >= "0" and del_inp <= "9":
    init.pop(int(del_inp)-1)
else:
    init.remove(del_inp)
print(f"""New color list: {", ".join(init)}""")