input_list = input("The original list: ").split()

def listSort(input_list):
    for k in range(0,len(input_list)):
        for a in range(0,len(input_list)-1):
            if input_list[k]>input_list[a]:
                continue
            else:
                b=input_list[k]
                input_list[k]=input_list[a]
                input_list[a]=b
    return input_list

input_list = list(map(int,input_list))
print("The sorted list: ",listSort(input_list))