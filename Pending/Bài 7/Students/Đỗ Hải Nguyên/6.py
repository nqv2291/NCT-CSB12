name=["BD","BTL","CG","DD",'HBT']
population=[274100,333300,266800,420900,318000]
area=[9.224,43.35,12.04,9.96,10.09]
avarage=0
print("Popluation density of:")
for i in range(len(name)):
    x=population[i]/area[i]
    print("- "+name[i]+":",x )
    avarage=avarage+x
avarage=avarage/len(name)
print('Average population density:',avarage)