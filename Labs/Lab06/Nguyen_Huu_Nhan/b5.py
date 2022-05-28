insert = input("Write a sentence:")
word_list = insert.split(' ')
b = len(word_list)
for i in range(len(word_list)):
    if word_list.count(word_list[i]) > 1:
       b = b - word_list.count(word_list[i]) + 1
       break
print (f"Number of unique word {b}")

