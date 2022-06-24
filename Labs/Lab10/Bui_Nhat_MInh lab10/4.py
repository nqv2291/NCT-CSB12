students = [
    {'firstName': 'Nikki', 'lastName': 'Roysden'},
    {'firstName': 'Mervin', 'lastName': 'Friedland'},
    {'firstName': 'Aron', 'lastName': 'Wilkins'}
]
print('List of students:')
for i in range(len(students)):
    print(f"- {students[i]['firstName']} {students[i]['lastName']}")
