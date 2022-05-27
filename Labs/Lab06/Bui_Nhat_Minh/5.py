sentence = input('Write a sentence: ')
arr = sentence.split(' ')
arr = list(dict.fromkeys(arr))
arr = [x for x in arr if x != '']
print(f'Number of unique words: {len(arr)}')
