def rearrange(num_list):
    new_list = []
    while num_list:
        minimum = num_list[0]  # arbitrary number in list 
        for x in num_list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        num_list.remove(minimum)
    return new_list


ori_list = [122,21,-11,-90,64,12]
print(f"The original list: {ori_list}")
print(f"The sorted list: {rearrange(ori_list)}")
