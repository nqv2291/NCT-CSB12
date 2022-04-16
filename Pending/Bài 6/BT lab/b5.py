# get input string
string = input("Write a sentence: ")
word_list = string.split()

# extract unique words into a new list
counted_list = []
for word in word_list:
    # only append not counted words
    if word not in counted_list:
        counted_list.append(word)
        
print(f"Number of unique words: {len(counted_list)}")