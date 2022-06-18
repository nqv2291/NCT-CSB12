def ex1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dic = {}
    for k in keys:
        for v in values:
            dic[k] = v
            values.remove(v)
            break
    return dic# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print(ex1())

def ex2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict3 = {**dict1,**dict2}
    return dict3# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(ex2())

def ex3():
    sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
                }
            }
        }
    }
    
    dict = sampleDict["class"]
    dict2 = dict['student']
    dict3 = dict2['marks']
    dict4 = dict3['history']

    return dict4
print(ex3())
    # print value of key 'history'

def ex4():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    return # a dictonary which has keys in keys list and values inferred from sample_dict

def ex5():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    return # key of the mimimum value in the dict 