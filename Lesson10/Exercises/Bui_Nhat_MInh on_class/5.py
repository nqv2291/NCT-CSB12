sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# Từ có giá trị nhỏ nhất trong từ điển
min_value = min(sample_dict, key=sample_dict.get)
print(min_value)
