# #########################
# ## EXAMPLE: iterating over tuples
# """
#     Get useful information from a tuple:
#     Count the number of people that Taylor Swift wrote songs for
#     in a period of time given in the tuple. 
# """
# #########################
# tswift = ((2014,"Katy"),
#           (2014, "Harry"),
#           (2012,"Jake"), 
#           (2010,"Taylor"), 
#           (2008,"Joe")) 

# # create empty tuple
# nums = ()
# words = ()

# # separate (tswift) into 2 sub-tuples
# for t in tswift:
#     # concatenating with a singleton tuple
#     nums = nums + (t[0],)   
#     # only add words haven't added before
#     if t[1] not in words:   
#         words = words + (t[1],)

# min_year = min(nums)
# max_year = max(nums)
# num_people = len(words)

# print("From", min_year, "to", max_year, 
#       "Taylor Swift wrote songs about", num_people, "people!")
