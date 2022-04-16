name=["BD","BTL","CG","DD",'HBT']
population=[274100,333300,266800,420900,318000]
max=0
min=274100
for i in range(0,len(population)):
    if population[i] >=max:
        max=population[i]
for i in range(0,len(population)):
    if population[i] <=min:
        min=population[i]
print("Indices of:")
print("-Most populated dist.: ",population.index(max))
print("-Least populated dist.:",population.index(min) )
print("Names of:")
print("-Most populated dist.: ",name[population.index(max)])
print("-Least populated dist.:",name[population.index(min)])