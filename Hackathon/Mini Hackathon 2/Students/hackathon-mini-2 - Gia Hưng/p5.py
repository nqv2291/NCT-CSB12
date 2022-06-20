disname = [ "BD" , "BTL" , "CG" , "DB" , "HBT"]
population = [ 247100 , 333300 , 266800 , 420900 ,  318000]

print(f"most populated dist is:  {population.index(max(population))}")
print(f"least populated dist is:  {population.index(min(population))}")

print(f"most populated dist is:  {disname[population.index(max(population))]}")
print(f"least populated dist is:  {disname[population.index(min(population))]}")