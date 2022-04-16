with open('names.txt', 'r') as rf:
    print('List of names:')
    for name in rf:
        print("- " + name.rstrip())