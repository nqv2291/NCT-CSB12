s = "welcome to welcome to to"
word_list = s.split(" ")
print(word_list)

counted_list = list()
for word in word_list:
    if word not in counted_list:
        counted_list.append(word)
        
print(f"number of unique words: {len(counted_list)}")