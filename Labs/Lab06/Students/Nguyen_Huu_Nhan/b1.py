arr = [0,1,2,3,4,5,6,7,8,9]
add2 = []
double = []
shift = arr[:]
for i in arr:
    i += 2
    add2.append(i)
for i in arr:
    i *= 2
    double.append(i)
del(shift[:2])
for i in range (2):
    shift.append(i)

print (f"Add 2: {add2}")
print (f"Shift 2: {shift}")
print (f"Multiply by 2: {double}")
    
    


