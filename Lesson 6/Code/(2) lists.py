#########################
## EXAMPLE: various list operations
## put print(L) at different locations to see how it gets mutated
#########################
# L1 = [2,1,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# L1.extend([0,6])


# L = [2,1,3,6,3,7,0]
# #L.remove(2)
# #L.remove(3)
# #del(L[1])
# print(L.pop())

# s = "I<3 cs"
# #print(list(s))
# print(s.split('<'))
# L = ['a', 'b', 'c']
# print(''.join(L))
# print('_'.join(L))

# L=[9,6,0,3]
# print(sorted(L))
# L.sort()
# L.reverse()




# #########################
# ## EXAMPLE: aliasing
# #########################
# a = 1
# b = a
# print(a)
# print(b)

# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)


# #########################
# ## EXAMPLE: cloning
# #########################
# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print(chill)
# print(cool)






# #########################
# ## EXAMPLE: sorting with/without mutation
# #########################
# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)






# #########################
# ## EXAMPLE: lists of lists of lists...
# #########################
# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)
# print(brightcolors)
# hot.append('pink')
# print(hot)
# print(brightcolors)


# ###############################
# ## EXERCISE: Test yourself by predicting what the output is and 
# ##           what gets mutated then check with the Python Tutor
# ###############################
# cool = ['blue', 'green']
# warm = ['red', 'yellow', 'orange']
# print(cool)
# print(warm)

# colors1 = [cool]
# print(colors1)
# colors1.append(warm)
# print('colors1 = ', colors1)

# colors2 = [['blue', 'green'],
#           ['red', 'yellow', 'orange']]
# print('colors2 = ', colors2)

# warm.remove('red') 
# print('colors1 = ', colors1)
# print('colors2 = ', colors2)

# for e in colors1:
#     print('e =', e)

# for e in colors1:
#     if type(e) == list:
#         for e1 in e:
#             print(e1)
#     else:
#         print(e)

# flat = cool + warm
# print('flat =', flat)

# print(flat.sort())
# print('flat =', flat)

# new_flat = sorted(flat, reverse = True)
# print('flat =', flat)
# print('new_flat =', new_flat)

# cool[1] = 'black'
# print(cool)
# print(colors1)
