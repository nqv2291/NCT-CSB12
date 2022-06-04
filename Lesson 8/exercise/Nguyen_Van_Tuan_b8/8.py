# 8.1
def display_message(a): 
    print(a, "I am learning about functions in python")

display_message("Tuan,")
# 8.2
def favorite_book(title):
    print("One of my favorite books is", title)

favorite_book("Alice in Wonderland.")
# 8.3
def make_shirt(size, message): 
    print(f"This T-shirt has size {size} and a message: {message}")

make_shirt("M", "TH School")
size = input()
message = input()
make_shirt(size, message)
# 8.4
def make_shirt(size = "large", message = "I love Python"): 
    print(f"This T-shirt has size {size} and a message: {message}")

make_shirt()
make_shirt("medium", message)
size = input()
message = input()
make_shirt(size, message)
# 8.5
def describe_city(city, country):
    print(city,"is the capital of",country)

describe_city("Reykjavik", "Iceland")
describe_city("London", "England")
describe_city("Washington, D.C", "US")

