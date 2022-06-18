from cgi import print_form
from random import sample


def ex1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    print(dic)
   
ex1()
def ex2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict3 = {**dict1, **dict2 }
    print(dict3)
    return # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
ex2()
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
    print(sampleDict["class"]["student"]["marks"]["history"])
ex3()
    # print value of key 'history'

def ex4():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]
    for i in range(len(keys)):
        print(sample_dict[keys[i]])
    return # a dictonary which has keys in keys list and values inferred from sample_dict
ex4()
def ex5():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    
    return # key of the mimimum value in the dict
ex5()