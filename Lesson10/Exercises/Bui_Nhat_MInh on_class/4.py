sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# Thư viện cần trả về
dictionary = dict(zip(keys, sample_dict.values()))
print(dictionary)
