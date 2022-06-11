my_list = [5, 1, 8, 92, -1, 30.]
def sort(my_list = [5, 1, 8, 92, -1, 30.]):
    for i in range(len(my_list)):
        for h in range(i + 1, len(my_list)):

            if my_list[i] > my_list[h]:
                my_list[i], my_list[h] = my_list[h], my_list[i]
    return my_list
print(f"Original list {my_list}")
print (f"Sorted list {sort(my_list)}")



                

