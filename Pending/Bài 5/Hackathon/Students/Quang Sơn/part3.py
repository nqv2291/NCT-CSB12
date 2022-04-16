#bài 1
x = float(input("input a number: "))
compare = x > 10
print(f"{x} is larger than 10: ", compare)
#bài 2
a = float(input("input a number: "))
check_even_number = a%2 == 0
print(f"{a} is an even number: ", check_even_number)
#bài 3
date = date = input("Date in MM/DD/YYYY format: ")
day = date[3:5]
month = date[0:2]
year = date[6:]

new_date = day + "/" + month + "/" + year
print(f"Date in DD/MM/YYYY format: {date}")