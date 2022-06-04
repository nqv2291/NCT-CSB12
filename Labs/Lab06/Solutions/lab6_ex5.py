# get input string
print('Write a sentence: ', end='')
input_str = input()
word_list = input_str.split(' ')

# extract unique words into a new list
counted_list = []
for word in word_list:
  if not (word in counted_list):  # only append not counted words
    counted_list.append(word)

print('Number of unique words:', len(counted_list))