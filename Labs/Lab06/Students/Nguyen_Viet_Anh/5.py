input_str = input("Write a sentence: ")
word_list = input_str.split(' ')
len1 = len(word_list)
len2 = len1

for i in word_list:
    a = word_list.count(i)
    if a >= 2:
        len2 = len1 - a + 1
print(f"Number of unique words: {len2}")