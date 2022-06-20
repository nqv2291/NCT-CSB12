from pickle import APPEND


disname = [ "BD" , "BTL" , "CG" , "DB" , "HBT"]
population = [ 247100 , 333300 , 266800 , 420900 ,  318000]
area = [ 9.224 , 43.35 , 12.04 , 9.96 , 10.09]
popudenss = []
for i in range(len(disname)):
    popera = population[i] / area[i]
    popudenss.append(popera)
    print(f"{disname[i]}: {popera}")

number = 0
for i in popudenss:
    number = i + number
print(number)
totaldist = len(disname)
print(totaldist)
popudense = number / totaldist
print(f"average population density is {popudense}")